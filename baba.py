import json
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
# import wget
# import os

options = Options()
options.add_argument("--headless")
driver = webdriver.Chrome(options=options)

driver.get("https://www.alibaba.com/products/plush.html?IndexArea=product_en")
time.sleep(1)

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(3)

items = driver.find_elements_by_css_selector(".J-offer-wrapper")

output = []

for item in items:
    try:
        productName = item.find_element_by_css_selector('h4').text
    except:
        productName = None

    try:
        productPrice = item.find_element_by_css_selector(
            '.elements-offer-price-normal__price').text
    except:
        productPrice = None

    try:
        imgDiv = item.find_element_by_css_selector('.seb-img-switcher__imgs')
        imgURL = imgDiv.get_attribute('data-image')
        imgURL = 'https:' + imgURL

        # Get full-sized images
        imgURL = imgURL.replace("_300x300.jpg", "")
        imgURL = imgURL.replace("_300x300.png", "")

        # Uncomment below to download images locally
        # destination = "images/" + imgURL.split("/")[-1]
        # if(os.path.exists(destination) != True):
        #     wget.download(imgURL, destination)
    except:
        imgDiv = None
        imgURL = None

    itemData = {
        "name": productName,
        "img": imgURL,
        "price": productPrice
    }

    output.append(itemData)


json.dump(output, open('products.json', 'w'), indent=2)
driver.close()
