import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

os.makedirs('explicit_links', exist_ok=True)
path = os.path.join('explicit_links', 'links.csv')


def scrape_youtube_videos(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    video_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('/watch?v='):
            video_links.append('https://www.youtube.com' + href)

    df = pd.DataFrame({'Video Links': video_links})
    df.to_csv(path, index=False)


q = input('Enter the query:\n> ')
scrape_youtube_videos(q)
