from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

import time
from time import sleep
from random import randint

options = Options()
driver = webdriver.Chrome(options=options)

url = 'https://bristol.nl/nl-nl/heren/schoenen/#twn|?tn_p=1'
driver.get(url)
sleep(randint(2, 3))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
Data = soup.find_all('div', {'class': 'twn-product-tile__image'})

image_urls = []

time.sleep(3)

numbs = 2

while True:
    try:
         # Scroll down slowly and smoothly
        height = driver.execute_script("return document.body.scrollHeight")
        for i in range(0, int(height * 0.90),150):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.3)

        url = 'https://bristol.nl/nl-nl/heren/schoenen/#twn|?tn_p=' + str(numbs)
        driver.get(url)
        sleep(randint(2, 3))

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        newData = soup.find_all('div', {'class': 'twn-product-tile__image'})
        Data.extend(newData)

        if numbs == 27:
            break

        numbs +=1

    except Exception as e:
        print(e)
        break

for review in Data:
    image_url = review.find('img', {'class': 'is-main'})['src']
    if image_url.startswith('http'):
        image_urls.append(image_url)

counter = 1
with open('sneaker_images_BristolVER2.0.txt', 'w') as f:
    for url in image_urls:
        f.write("%s\n" % (url))
        counter += 1

driver.quit()
