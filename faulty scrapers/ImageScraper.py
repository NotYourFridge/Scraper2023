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
driver = webdriver.Chrome(options = options) 

url = 'https://www.decathlon.nl/browse/c0-heren-sportkleding/c1-sportschoenen-heren/_/N-17bmg12'
driver.get(url)
sleep(randint(2,3))


html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.find_all('div', {'class': 'product-list pl-list js-first svelte-1wkvbov'})

image_urls = []

while True:
    try:
        load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/main/div[2]/section[2]/nav[2]/button[2]')))
        load_more_button.click()
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews.extend(soup.find_all('div', {'class': 'product-list pl-list js-first svelte-1wkvbov'}))

        time.sleep(2)
    except Exception as e:
        print(e)
        break
        

for review in reviews:
    image_url = review.find('img', {'class': 'svelte-11itto'})['src']
    image_urls.append(image_url)

    with open('sneaker_images.txt', 'w') as f:
        for url in image_urls:
            f.write("%s\n" % url)

driver.quit()

