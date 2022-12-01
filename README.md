# Valorant YouTube Comments
## Data Acquisition and Pre-processing for Sentiment Analysis

The VALORANT-COMMENTS script gets videos and comments for list of YouTuber data provided in CSV form from the YouTube API v3. Sentiment_Analysis_Preprocess preprocesses the acquired data for sentiment analysis

## Team Members
- Amira Bendjama
- Nicole Padilla

## Introduction
Utilizing the YouTube API v3 and a user-determined file of YouTubers this project collects the comment data from a selection of YouTubers streaming the popular game Valorant.

Youtube is one the leading digital content platforms. Its engaging, visual platform has made it a dominant player in the gaming industry - one of the largest markets in the world. YouTube has over 40 million active gaming channels. Globally, there have been over 100 billion hours of gaming content watched on YouTube. Consequently, YouTube is an important platform for game marketing. The instant, candid feedback available via the comment section is a particularly ripe area for market research. Our project looks to showcase how a large gaming company, Riot games, could utilize data from YouTube comments to garner detailed market feedback on its first-person shooter game Valorant. We plan to focus on a selection of large and small gaming YouTubers playing Valorant and analyze the comment section of their videos. This will collect unique information, not available to Riot through its own YouTube channels, as well as provide insights into potential marketing channels (i.e. through influencer-style partnerships or advertising placements with the identified YouTubers).

## Features

### VALORANT-COMMENTS.ipynb
Collect comment data from YouTube API

#### REQUIREMENTS:
-You must first get an API Key for the YouTube API (https://developers.google.com/youtube/v3/getting-started)

Libraries:
- Pandas
- googleapiclient.discovery
- requests
- BeautifulSoup
- re
- json

Files:
##### YouTubers.csv
User-generated file that contains list of YouTubers, subscriber count and URL
##### keys.txt
List of unique API Keys from YouTube API

#### RESULTS:

##### channels.csv
For each YouTuber in YouTubers.csv columns:
"channel_id" 
"channel_title"
"channel_subscriber_count"
"channel_video_count"
"channel_view_count"

##### videos.csv
For each video from each channel in channels.csv columns:
Title
Channel Title
Channel ID
Publish time 
Duration 
Number of comments 
Number of likes 
Number of views 
video_id 
url

##### comments.csv
For each comment on each video in videos.csv columns:
"Comment ID"
"Comment"
"Likes"
"Replies"
"Channel ID"
"Video ID"

##### comments_videos_channel_info.csv
Merges all data from channel.csv, videos.csv and comments.csv for further analysis

### Sentiment_Analysis_Preprocess.ipynb
Pre-process comment data for Sentiment Analysis

#### REQUIREMENTS
Libraries: 
- csv
- pandas
- demoji
- re
- contractions
- nltk
 - nltk.download('stopwords')
 - nltk.download('wordnet')
 - nltk.download('omw-1.4')
 - from nltk.corpus import stopwords
 - from nltk.stem import WordNetLemmatizer
 Files:
 - comments_videos_channel_info.csv (result of Valorant-Comments)
 
#### RESULTS

.txt files grouped by channel containing text ready for sentiment analysis

## Running the Scripts
- Set up your API with YouTube & get API Keys. Create keys.txt file containing keys
- Utilize provided YouTubers.csv that contains:YouTuber, subscriber count and URL
- Run Valorant-Comments.ipynb step by step. In-file markdown provides installation of libraries as needed and documentation of each function. You must provide updated keys.txt with your own keys and YouTubers.csv.
- Valorant-Comments will generate final dataset for analysis : comments_videos_channel_info.csv
- Run Sentiment_Analysis_Preprocessing.ipynb with comments_videos_channel_info.csv. In-file markdown provides installation of libraries as needed and documentation of each function.

 
## Sample data
Sample output data can be found in github under the data file
### Valorant-Comments Results:
#### channels.csv
For each YouTuber in YouTubers.csv columns: "channel_id" "channel_title" "channel_subscriber_count" "channel_video_count" "channel_view_count"

#### videos.csv
For each video from each channel in channels.csv columns: Title Channel Title Channel ID Publish time Duration Number of comments Number of likes Number of views video_id url

#### comments.csv
For each comment on each video in videos.csv columns: "Comment ID" "Comment" "Likes" "Replies" "Channel ID" "Video ID"

#### comments_videos_channel_info.csv
Merges all data from channel.csv, videos.csv and comments.csv for further analysis

### Sentiment_Analysis_Preprocess Results:
.txt files grouped by channel containing text ready for sentiment analysis

## Use Cases
The goal of collecting the Valorant comment data from the YouTube API is to make it available for sentiment analysis. This sentiment analysis may be interesting to marketers, both of games and products targeted at gamers, streamers looking to improve their popularity or gaming companies seeking feedback.
Some potential applications include, to improve the marketing strategies for gaming companies, especially Riot games by providing data on YouTubers playing one of their popular games. It could be used to identify partnerships for promotions, to target ad placements or to see the contrast of the overall sentiment about the game between youtubers with different number counts.
## Data Origins
Raw comment data from YouTube API v3
### Criteria for picking streamers:
- Only verified channels, with a lower bound of subscription count of 100k, since the latter is how much the channel must reach in order to be eligible to apply for verification, and companies and brands will only consider verified channel to promote their products, in our case games.
- Most Valorant streamers are based on twitch, so a popular twitch streamers doesn’t qualify as a popular youtuber, so we picked Valorant youtubers that upload on their main YouTube channel and have a certain subscription count.
- The Valorant youtubers are split into two categories: Big youtubers above 500k subscription count, and small youtubers are under and above 100k.
YouTubers are English speakers from around the world, so it is not based on location but language.
- YouTube channels are mixed between channels with only Valorant videos, and channels with variety of other content besides Valorant. Mainly to see the comment section through different communities.

## Issues & Limitations
### Limits in Acquiring Data
- We are limited in how much data we can pull because we are using the free version of the YouTube API and it has a daily quota. Videos with very large numbers of comments can quickly max out our daily call count.
#### Limits in Utilizing Data
- Comment sections are full of misspellings, slang terms, troll comments etc. that can confuse the results of sentiment analysis. We have attempted to clean the data as much as possible to handle this
- Emojis cannot be understood by the sentiment analysis tools we are aware of, so while they make up a lot of comment data they must be removed for analysis.

## Distribution & Access Rights
Our choice of the YouTube API as the source of our data gives us confidence that our data can be publicly accessed and distributed. We selected only data identified by YouTube as public.

We have chosen to distribute our data on GitHub

## Conclusion
This project has given us an excellent tutorial in the challenges of working with APIs and their limitations as well as helped us to learn about the requirements, difficulties and considerations, of data pre-processing for sentiment analysis. This has been a useful excercise in growing our data science skills and allowed us to return an interesting dataset that could be recreated in different ways to answer many interesting questions.






