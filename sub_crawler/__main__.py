import urllib

from bs4 import BeautifulSoup

hdr = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}

url = 'https://www.subway.com/nl-NL/MenuNutrition/Menu/Sub-of-the-Day'

request = urllib.request.Request(url, headers=hdr)
page = urllib.request.urlopen(request)
soup = BeautifulSoup(page, 'html.parser')

rawData = soup.find_all('h3', {'class': 'menu-cat-prod-title'})


data = list(map(lambda x: x.text, rawData))

print(data)
