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

url = 'https://www.decathlon.nl/browse/c0-heren-sportkleding/nature-schoenen/_/N-178c3k0Z1fnlr4v'
driver.get(url)
sleep(randint(2, 3))

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
Data = soup.find_all('div', {'class': ['vtmn-relative vtmn-h-0 svelte-slvulf','dpb-models vtmn-relative svelte-310lux']})
Data += soup.find_all('a', {'class': 'vtmn-absolute vtmn-top-0 vtmn-left-0 vtmn-h-full vtmn-w-full'})

image_urls = []

while True:
    try:
         # Scroll down slowly and smoothly
        height = driver.execute_script("return document.body.scrollHeight")
        for i in range(0, int(height * 0.45),15):
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(0.005)

        load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="app"]/main/div[2]/section[2]/nav[2]/button[2]')))
        load_more_button.click()

        time.sleep(2.5)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        newData = soup.find_all('div', {'class': ['vtmn-relative vtmn-h-0 svelte-slvulf','dpb-models vtmn-relative svelte-310lux']})
        newData += soup.find_all('a', {'class': 'vtmn-absolute vtmn-top-0 vtmn-left-0 vtmn-h-full vtmn-w-full'})
        Data.extend(newData)

    except Exception as e:
        print(e)
        break

for review in Data:
    image_url = review.find('img', {'class': ['svelte-11itto', 'lz svelte-11itto lz-ldd']})['src']
    if image_url.startswith('http'):
        image_urls.append(image_url)

counter = 1
with open('sneaker_images_decathlon.txt', 'w') as f:
    for url in image_urls:
        f.write("%d. %s\n" % (counter, url))
        counter += 1

driver.quit()