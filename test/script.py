from googleapiclient.discovery import build
import pandas as pd


def scrape_youtube_videos(query):
    api_key = 'YOUR_API_KEY'
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

    df = pd.DataFrame({'Video Links': video_links})
    df.to_csv('fruit_videos.csv', index=False)


scrape_youtube_videos('fruits')
