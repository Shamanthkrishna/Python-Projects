# YT_Extracter.py
from googleapiclient.discovery import build
from pytube import YouTube, Channel
import pandas as pd

api_key = 'Your_API_Goes_Here'          
youtube = build('youtube', 'v3', developerKey=api_key)

def get_channel_id(video_url):
    """Get YouTube channel ID from video URL."""
    try:
        yt = YouTube(video_url)
        channel = Channel(yt.channel_url)
        return channel.channel_id
    except Exception as e:
        raise Exception(f"Failed to get channel ID: {e}")

def getChannelStats(youtube, channel_ids):
    """Get statistics for the given list of channel IDs."""
    all_data = []
    try:
        request = youtube.channels().list(
            part='snippet,contentDetails,statistics',
            id=','.join(channel_ids)
        )
        response = request.execute()

        for item in response['items']:
            data = dict(
                Channel_Name=item['snippet']['title'],
                Subscribers=item['statistics']['subscriberCount'],
                Views=item['statistics']['viewCount'],
                Total_Videos=item['statistics']['videoCount']
            )
            all_data.append(data)
    except Exception as e:
        raise Exception(f"Failed to get channel stats: {e}")
    
    return all_data

def dataProcess(channel_ids):
    """Process data and convert to DataFrame."""
    try:
        channel_statistics = getChannelStats(youtube, channel_ids)
        channel_data = pd.DataFrame(channel_statistics)
        channel_data['Subscribers'] = pd.to_numeric(channel_data['Subscribers'])
        channel_data['Views'] = pd.to_numeric(channel_data['Views'])
        channel_data['Total_Videos'] = pd.to_numeric(channel_data['Total_Videos'])
        return channel_data
    except Exception as e:
        raise Exception(f"Failed to process data: {e}")

def export_to_csv(data, filename='channel_data.csv'):
    """Export DataFrame to CSV."""
    try:
        data.to_csv(filename, index=False)
        print(f"Data exported to {filename}")
    except Exception as e:
        raise Exception(f"Failed to export data: {e}")
