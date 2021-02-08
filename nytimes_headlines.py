import requests
from bs4 import BeautifulSoup

r = requests.get('https://nytimes.com')

soup = BeautifulSoup(r.text, "html.parser")


def cleanHeadlines(h):
    # Kind of a hacky way to do this, just assuming that any actual headlines are going to be of a certain length
    return len(h.text) > 20


headlines = soup.select('h3')
headlines = filter(cleanHeadlines, headlines)

for headline in headlines:
    print(headline.text)
