from bs4 import BeautifulSoup
import requests

site_url = 'https://www.youtube.com/'
site_html = requests.get(site_url).text
# print(site_html)
soup = BeautifulSoup(site_html, 'lxml')
print(soup.prettify())
# videos = soup.find('div', class_ = 'style-scope ytd-rich-grid-renderer')
# print(videos)
