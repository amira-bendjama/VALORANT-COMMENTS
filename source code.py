import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
# pip install --upgrade google-api-python-client
from googleapiclient.discovery import build
import os


# each time call the service pop keys
def get_service():
    global youtube_service
    if keys:
        youtube_service = youtube_build_service(keys.pop())


def get_keys(file_path):
    with open('data/keys.txt', "r") as f:
        keys = f.read()
    keys = keys.split("\n")
    return keys


def get_channels_names(file_path):
    youtubers = pd.read_csv(file_path, sep=",", header=0)
    return youtubers


def get_channel_id(channel_url):
    url = ""
    # getting json
    resp = requests.get(channel_url)
    data = BeautifulSoup(resp.text, "html.parser")
    # finding "externalId" that has the channel id no matter what is link structure
    data_s = str(data)

    search_url = re.search('"externalId":', data_s)
    start, end = search_url.span()
    # finding the url after the id, using index
    for i in range(end, end + 100):
        if data_s[i] == ",":
            break
        url += data_s[i]
    url = url.split('"')[1]
    return url


def get_channels_details_info(youtubers, youtube_service):
    dict_youtubers = {}
    l_youtubers = []
    for index in range(len(youtubers["url"])):
        # get the channel ID from the URL
        channel_id = get_channel_id(youtubers["url"].iloc[index])
        # get the channel details
        response = get_channel_details(youtube_service, id=channel_id)
        snippet = response["items"][0]["snippet"]
        statistics = response["items"][0]["statistics"]
        dict_youtubers = {
            "channel_id": channel_id,
            "channel_title": snippet["title"],
            "channel_subscriber_count": statistics["subscriberCount"],
            "channel_video_count": statistics["videoCount"],
            "channel_view_count": statistics["viewCount"]
        }
        l_youtubers.append(dict_youtubers)

    return l_youtubers


def get_channel_details(youtube, **kwargs):
    return youtube.channels().list(
        part="statistics,snippet,contentDetails",
        **kwargs
    ).execute()


# building youtube service
def youtube_build_service(KEY):
    YOUTUBE_API_SERVICE_NAME = "youtube"
    YOUTUBE_API_VERSION = "v3"

    return build(YOUTUBE_API_SERVICE_NAME,
                 YOUTUBE_API_VERSION,
                 developerKey=KEY)


def get_channel_videos(youtube, **kwargs):
    return youtube.search().list(
        **kwargs
    ).execute()


def get_video_details(youtube, **kwargs):
    return youtube.videos().list(
        part="snippet,contentDetails,statistics",
        **kwargs
    ).execute()


def video_infos(video_response):
    items = video_response.get("items")[0]
    # get the snippet, statistics & content details from the video response
    snippet = items["snippet"]
    statistics = items["statistics"]
    content_details = items["contentDetails"]
    # get infos from the snippet
    channel_title = snippet["channelTitle"]
    channel_id = snippet["channelId"]
    title = snippet["title"]
    publish_time = snippet["publishedAt"]

    # get stats infos
    comment_count = statistics["commentCount"]
    like_count = statistics["likeCount"]
    view_count = statistics["viewCount"]
    # get duration from content details
    duration = content_details["duration"]

    # duration in the form of something like 'PT5H50M15S'
    # parsing it to be something like '5:50:15'
    parsed_duration = re.search(f"PT(\d+H)?(\d+M)?(\d+S)?", duration).groups()
    duration_str = ""
    for d in parsed_duration:
        if d:
            duration_str += f"{d[:-1]}:"
    duration_str = duration_str.strip(":")

    dict_video_info = {
        "Title": title,
        "Channel Title": channel_title,
        "Channel ID": channel_id,
        "Publish time": publish_time,
        "Duration": duration_str,
        "Number of comments": comment_count,
        "Number of likes": like_count,
        "Number of views": view_count

    }

    return dict_video_info


def get_videos_from_channel(youtube_service, channel_id, videos_limit=5):
    # counting number of videos grabbed
    n_videos = 0
    next_page_token = None
    list_videos = []

    while n_videos < videos_limit:
        # paramters to select the videos
        # only valorant related videos
        params = {
            'part': 'snippet',
            'q': 'valorant',
            'channelId': channel_id,
            'type': 'video',
        }

        if next_page_token:
            params['pageToken'] = next_page_token

        try:
            # getting channel videos based on parameters
            res = get_channel_videos(youtube_service, **params)
            # getting items
            channel_videos = res.get("items")

            for video in channel_videos:
                if n_videos == videos_limit:
                    break

                video_id = video["id"]["videoId"]
                # easily construct video URL by its ID
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                video_response = get_video_details(youtube_service, id=video_id)

                # get video details in dictionary
                dictionary_video = video_infos(video_response)
                dictionary_video["video_id"] = video_id
                dictionary_video["url"] = video_url
                # changed just location
                n_videos += 1

                list_videos.append(dictionary_video)

            # if there is a next page, then add it to our parameters
            # to proceed to the next page
            if "nextPageToken" in res:
                next_page_token = res["nextPageToken"]
        # catch the quota exception and switch keys
        except Exception as e:
            if keys:
                print("switching keys", len(list_videos))
                get_service()
                continue
            else:
                print("break", len(list_videos))
                return list_videos

    return list_videos


def get_comments(youtube, **kwargs):
    return youtube.commentThreads().list(
        part="snippet",
        **kwargs
    ).execute()


def get_comments_video(videoId, total_comments=10000, max_comment_per_page=100, order="time"):
    comments_nb = 0

    list_comments = []
    comments_dict = {}

    while comments_nb < total_comments:

        params = {
            'videoId': videoId,
            'maxResults': max_comment_per_page,
            'order': 'relevance',  # default is 'time' (newest)
        }
        try:
            response = get_comments(youtube_service, **params)

            items = response.get("items")

            # if items is empty, breakout of the loop
            if not items:
                break

            for item in items:
                if comments_nb == total_comments:
                    break
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comment_id = item['snippet']['topLevelComment']['id']
                reply_count = item['snippet']['totalReplyCount']
                like_count = item['snippet']['topLevelComment']['snippet']['likeCount']

                comments_dict = {
                    "Comment ID": comment_id,
                    "Comment": comment,
                    "Likes": like_count,
                    "Replies": reply_count,
                    "Video ID": videoId
                }
                comments_nb += 1
                list_comments.append(comments_dict)

            if "nextPageToken" in response:
                # if there is a next page
                # add next page token to the params we pass to the function
                params["pageToken"] = response["nextPageToken"]

            else:
                # must be end of comments!!!!
                break

        except Exception:
            if keys:
                #                 print("switching keys", len(list_comments))
                get_service()
                continue
            else:
                #                 print("break",len(list_comments) )
                return list_comments

    return list_comments


if __name__ == '__main__':
    youtubers = get_channels_names("data/Youtubers.csv")
    keys = get_keys('data/keys.txt')
    # call this function to build the service
    # and also to switch keys
    get_service()

    if os.path.exists("data/channels_info.csv"):
        # load any pre-existing data
        df = pd.read_csv('data/channels_info.csv')
        df.pop(df.columns[0])
    else:
        channels_info = get_channels_details_info(youtubers, youtube_service)
        df = pd.DataFrame(channels_info)
        # save to csv file
        df.to_csv('data/channels_info.csv', index=False)

    if os.path.exists("data/videos_info.csv"):
        # load any pre-existing data
        df_videos = pd.read_csv('data/videos_info.csv')
        # dropping the index column
        df_videos.pop(df_videos.columns[0])
    else:
        videos_retrieved = []
        # don't forget to remove the -2 index when you remove the two last small youtubers
        for channel_id in df["channel_id"][:-2]:
            videos_retrieved.extend(get_videos_from_channel(youtube_service, channel_id, 21))
            print("next video")
            print()

        df_videos = pd.DataFrame(videos_retrieved)
        # save to csv file
        df_videos.to_csv('data/videos_info.csv', index=False)

    if os.path.exists("data/comments.csv"):
        # load any pre-existing data
        df_comments = pd.read_csv('data/comments.csv')
        df_comments.pop(df_comments.columns[0])
    else:
        comments = []
        #     comments.extend(get_comments_video("DTuS6Bki9kI", 684))

        for i, video_id in enumerate(df_videos["video_id"]):
            #         print("next video")
            comments.extend(get_comments_video(video_id, df_videos["Number of comments"][i]))

        df_comments = pd.DataFrame(comments)
        df_comments.to_csv('data/comments.csv', index=False)
