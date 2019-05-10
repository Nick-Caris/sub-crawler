import urllib
from functools import lru_cache

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

@lru_cache(maxsize=1)
def crawl(weeknr):
    print("New Week!, getting a new list")
    page = urllib.request.urlopen(request)
    rawData = BeautifulSoup(page, 'html.parser').find_all(
        'h3', {'class': 'menu-cat-prod-title'})
    return [x.text for x in rawData]
