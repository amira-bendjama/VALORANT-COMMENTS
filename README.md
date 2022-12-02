# Valorant YouTube Comments
![Screenshot](https://valorantstrike.com/wp-content/uploads/2020/08/Valorant-Wallpaper-Girls-Dark-Display.jpg)
### Data Acquisition and Pre-processing for Sentiment Analysis
This project collects the most recent comments and videos from a selection of Youtubers streaming the popular game Valorant, utilizing Youtube API v3 and a user-defined file of Youtubers.
## Table of Contents
  * [Introduction](#introduction)
  * [Features](#features)
  * [REQUIREMENTS](#requirements)
    + [Installation](#installation)
  * [Running the Scripts](#running-the-scripts)
  * [Data Tables](#data-tables)
        * [CHANNEL TABLE](#channel-table)
        * [VIDEO TABLE](#video-table)
        * [COMMENTS TABLE](#comments-table)
  * [Data collection](#data-collection)
    + [DATASET RESULT FILES](#dataset-result-files)
  * [Use Cases](#use-cases)
    + [Criteria for picking streamers](#criteria-for-picking-streamers)
  * [Issues & Limitations](#issues---limitations)
    + [Limits in Acquiring Data](#limits-in-acquiring-data)
    + [Limits in Utilizing Data](#limits-in-utilizing-data)
  * [Distribution & Access Rights](#distribution---access-rights)
  * [Conclusion](#conclusion)
  * [Contributors ✨](#contributors--)
 
## Introduction
Our project looks to showcase how a large gaming company, Riot games, could utilize data from YouTube comments to garner detailed market feedback on its first-person shooter game Valorant. We focused on selectioning large and small gaming YouTubers playing Valorant, where we collected their most recent videos about the game valorant and retrieved their comments. This collected unique information, not available to Riot through its own YouTube channels, as well as provide insights into potential marketing channels (i.e. through influencer-style partnerships or advertising placements with the identified YouTubers).

## Features
- Import Valorant Youtuber of your liking or use the file Youtubers.csv in data folder.
- Collect Youtubers channel inforamtion such as total videos, total view, subscription count in a CSV file.
- Collect most recent 30 videos relating to Valorant in each channel, that will contain all the imortant information about the latter such as video total view count, total likes, total comments, video URL. 
- Retrieve all the comments of the collected videos, which will have information about the comments such as comment text, total likes, total replies. 
- **NICOLE WRITE YOUR FEATURES**

## REQUIREMENTS
In this project, we used Youtube API to retrieve comments, and videos from channels. We mainly used [youtube guide](https://developers.google.com/youtube/v3/getting-started), and other [ressources](https://towardsdatascience.com/how-to-build-your-own-dataset-of-youtube-comments-39a1e57aade). 
In order to access the API, a project must be created in [Google Developer’s Console](https://console.cloud.google.com/apis/dashboard?project=caramel-logic-370101), where you will have to do two steps: 
* Enable Youtube API data API v3.
* Create API key.

### Installation
 Install libraries for Google API client for python
```  
pip install --upgrade google-api-python-client
```
**NICOLE ADD YOUR PIP INSTALLATION HERE**
``` 
other pip
nltk.download(‘stopwords’)
nltk.download(‘wordnet’)
nltk.download(‘omw-1.4’)
```  
Libraries used:
``` 
Pandas
googleapiclient.discovery
requests
BeautifulSoup
re
json
csv
pandas
demoji
re
contractions
nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
``` 
## Running the Scripts
1.  Create keys.txt file containing your generated keys from the requirement section.
2. Utilize provided YouTubers.csv that contains: YouTuber, subscriber count and URL
3. Run Valorant-Comments.ipynb step by step that contains documentation of each function and provides installation of libraries as needed. 
4. Valorant-Comments will generate 4 dataset: channels, videos, comments, and comments_videos_channel_info, which is joined table of the 3 tables .
5. Run Sentiment_Analysis_Preprocessing.ipynb with comments_videos_channel_info.csv. In-file markdown provides installation of libraries as needed and documentation of each function.

## Data Tables
The design follows these general principles.  Each youtuber, channel and comments is assigned a unique number (Channel ID, Video ID, Comment ID).All of the information relating to the latters are joined in one table comments_videos_channel_info.csv. The Channel IDs are linked to Video tables and each comment ID is linked to videos table.

The database is comprised of the following main tables:
  - Youtubers - channel names, urls, subscription count
  - channel - all information for channel
  - videos - videos from each channel
  - comments - all comments from each video

##### CHANNEL TABLE 
For each YouTuber in YouTubers.csv:

    channel_id unique           channel unique code
    channel_title               channel title
    channel_subscriber_count    channel subscribers count
    channel_video_count         total videos in the channel
    channel_view_count          total views of all videos in the channel

##### VIDEO TABLE  
For each video from each channel in channels.csv columns:

    Title                       video title
    Channel Title               channel title       
    Channel ID                  channel unique code     
    Publish time                published date for video 
    Duration                    duration of the video  
    Number of comments          total comments in the video             
    Number of likes             total likes of the video          
    Number of views             total views of video          
    video_id                    video unique code  
    url                         link to the video

##### COMMENTS TABLE  
For each comment on each video in videos.csv columns:

    Comment ID                  comment unique code       
    Comment                     comment text    
    Likes                       comment total likes   
    Replies                     comment total replies    
    Channel ID                  channel unique code       
    Video ID                    video unique code    
## Data collection 
Initial data was gathered via the YouTube API v3 which allows publicly available YouTube comments to be called by anyone who created an app with their Google account. [GeeksforGeeks](https://www.geeksforgeeks.org/how-to-extract-youtube-comments-using-youtube-api-python/) was used as a reference for the code written to run the API call. The code was modified and resulting data was loaded into a .csv file.
### DATASET RESULT FILES
In our project, there are **22 Youtubers** selected based on their subscription count. we collected infomration of each channel, and retrieved **30 most recent videos** related to Valorant from each channel, and fetched all the comments from the channels which generated **281480 comments.**
| file name        | description| path  |
| ------------- |:-------------:| -----:|
| Youtubers.csv| contains all youtubers information | /data/Youtubers.csv |
| channels.csv | For each YouTuber in YouTubers.csv columns: "channel_id" "channel_title" "channel_subscriber_count" "channel_video_count" "channel_view_count"     |   /data/channels.csv|
| videos.csv | For each video from each channel in channels.csv columns: Title Channel Title Channel ID Publish time Duration Number of comments Number of likes Number of views video_id url   |    /data/videos.csv |
| comments.csv | or each comment on each video in videos.csv columns: "Comment ID" "Comment" "Likes" "Replies" "Channel ID" "Video ID"  |    /data/comments.csv |
| comments_videos_channel_info.csv | Merges all data from channel.csv, videos.csv and comments.csv for further analysis  |/data/comments_videos_channel_info.csv |

**add text files here**
.txt files grouped by channel containing text ready for sentiment analysis

## Use Cases
The goal of collecting the Valorant comment data from the YouTube API is to make it available for sentiment analysis. This sentiment analysis may be interesting to marketers, both of games and products targeted at gamers, streamers looking to improve their popularity or gaming companies seeking feedback.
Some potential applications include, to improve the marketing strategies for gaming companies, especially Riot games by providing data on YouTubers playing one of their popular games. It could be used to identify partnerships for promotions, to target ad placements or to see the contrast of the overall sentiment about the game between youtubers with different number counts.

### Criteria for picking streamers
- Only verified channels, with a lower bound of subscription count of 100k, since the latter is how much the channel must reach in order to be eligible to apply for verification, and companies and brands will only consider verified channel to promote their products, in our case games.
- Most Valorant streamers are based on twitch, so a popular twitch streamers doesn’t qualify as a popular youtuber, so we picked Valorant youtubers that upload on their main YouTube channel and have a specific subscription count.
- The Valorant youtubers are split into two categories: Big youtubers above 500k subscription count, and small youtubers are under and above 100k.
YouTubers are English speakers from around the world, so it is not based on location but language.
- YouTube channels are mixed between channels with only Valorant videos, and channels with various other content besides Valorant. Mainly to see the comment section through different communities.

## Issues & Limitations
### Limits in Acquiring Data
- We are limited in how much data we can pull because we are using the free version of the YouTube API and it has a daily quota. Videos with very large numbers of comments can quickly max out our daily call count.

### Limits in Utilizing Data
- Comment sections are full of misspellings, slang terms, troll comments etc. that can confuse the results of sentiment analysis. We have attempted to clean the data as much as possible to handle this
- Emojis cannot be understood by the sentiment analysis tools we are aware of, so while they make up a lot of comment data they must be removed for analysis.

## Distribution & Access Rights
Our choice of the YouTube API as the source of our data gives us confidence that our data can be publicly accessed and distributed. We selected only data identified by YouTube as public.

We have chosen to distribute our data on GitHub

## Conclusion
This project has given us an excellent tutorial in the challenges of working with APIs and their limitations as well as helping us to learn about the requirements, difficulties and considerations, of data pre-processing for sentiment analysis. This has been a useful exercise in growing our data science skills and allowed us to return an interesting dataset that could be recreated in different ways to answer many interesting questions.


## Contributors ✨
- Amira Bendjama 
- Nicole Padilla
