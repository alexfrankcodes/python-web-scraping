import requests
from bs4 import BeautifulSoup
import time

url = 'https://sfbay.craigslist.org/d/admin-office/search/ofc'


def get_page(url, start):
    params = {
        's': start
    }

    r = requests.get(url, params=params)
    soup = BeautifulSoup(r.text, 'html.parser')

    titles = soup.select('.result-title')

    output = [title.text.strip() for title in titles]

    return output


start = 0

while True:
    jobs = get_page(url, start)

    if len(jobs) == 0:
        break

    for job in jobs:
        print(job)

    start += 120

    time.sleep(1)
