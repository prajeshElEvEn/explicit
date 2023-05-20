from googleapiclient.discovery import build
import pandas as pd
import os

os.makedirs('data', exist_ok=True)

data_path = os.path.join('data', 'links.csv')


def scrape_youtube_videos(query):
    api_key = os.environ.get("YOUTUBE_API_KEY")
    youtube = build('youtube', 'v3', developerKey=api_key)

    video_links = []
    next_page_token = None

    while True:
        search_response = youtube.search().list(
            q=query,
            type='video',
            part='id',
            maxResults=50,
            pageToken=next_page_token
        ).execute()

        for item in search_response['items']:
            video_links.append(
                'https://www.youtube.com/watch?v=' + item['id']['videoId'])

        next_page_token = search_response.get('nextPageToken')

        if not next_page_token:
            break

    df = pd.DataFrame({'links': video_links})
    df.to_csv(data_path, index=True, index_label='index')


q = input("Enter the query:\n> ")
scrape_youtube_videos(q)
