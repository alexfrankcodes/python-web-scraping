import requests
from bs4 import BeautifulSoup
import time

craigslistURL = 'https://sfbay.craigslist.org'
r = requests.get(craigslistURL)

soup = BeautifulSoup(r.text, "html.parser")

links = soup.select("#jjj0 a")

for link in links:
    jobCategories = link.text
    jobURL = craigslistURL + link.get("href")

    jobRequest = requests.get(jobURL)
    jobSoup = BeautifulSoup(jobRequest.text, "html.parser")
    total = jobSoup.select_one(".totalcount").text
    print(jobCategories, total)

    time.sleep(1)
