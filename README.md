# VALORANT COMMENTS - Data collection & Pre-processing

The VALORANT-COMMENTS script gets videos and comments for list of YouTuber data provided in CSV form from the YouTube API v3. Sentiment_Analysis_Preprocess preprocesses the acquired data for sentiment analysis

## VALORANT-COMMENTS.ipynb
Collect comment data from YouTube API

### REQUIREMENTS:
-You must first get an API Key for the YouTube API (https://developers.google.com/youtube/v3/getting-started)

Libraries:
--Pandas
--googleapiclient.discovery
--requests
--BeautifulSoup
--re
--json

Files:
#### YouTubers.csv
User-generated file that contains list of YouTubers, subscriber count and URL
#### keys.txt
List of unique API Keys from YouTube API

### RESULTS:

#### channels.csv
For each YouTuber in YouTubers.csv columns:
"channel_id" 
"channel_title"
"channel_subscriber_count"
"channel_video_count"
"channel_view_count"

### videos.csv
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

### comments.csv
For each comment on each video in videos.csv columns:
"Comment ID"
"Comment"
"Likes"
"Replies"
"Channel ID"
"Video ID"

### comments_videos_channel_info.csv
Merges all data from channel.csv, videos.csv and comments.csv for further analysis

## Sentiment_Analysis_Preprocess.ipynb
Pre-process comment data for Sentiment Analysis

### REQUIREMENTS
csv
pandas
demoji
re
contractions
nltk
 nltk.download('stopwords')
 nltk.download('wordnet')
 nltk.download('omw-1.4')
 from nltk.corpus import stopwords
 from nltk.stem import WordNetLemmatizer
 
### RESULTS

File: Preprocessed_Data
-.txt files grouped by channel containing text ready for sentiment analysis





