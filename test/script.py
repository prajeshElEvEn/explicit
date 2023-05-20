import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

os.makedirs('data', exist_ok=True)

data_path = os.path.join('data', 'video_links.csv')


def scrape_youtube_videos(query):
    url = f"https://www.youtube.com/results?search_query={query}"
    # print("[+] url: ",url)
    response = requests.get(url)
    # print("[+] response: ",response)
    soup = BeautifulSoup(response.text, 'html.parser')
    # print("[+] soup: ",soup)
    video_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('/watch?v='):
            video_links.append('https://www.youtube.com' + href)

    # print("[+] video_links: ",video_links)

    df = pd.DataFrame({'Video Links': video_links})
    df.to_csv(data_path, index=False)


q = input("Enter the query:\n> ")
scrape_youtube_videos(q)
