import json
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

url = 'https://www.vans.nl/shop/nl/vans-nl/heren-schoenen/old-skool-schoenen-vn000d3hy28#'
driver.get(url)
sleep(randint(2,3))

reviews = []

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.find_all('section', {'class': 'pr-review-display pr-rd-display-desktop'})


while True:
    try:
        # locate the "Load More" button and click it
        load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pr-review-display"]/footer/div/div/a')))
        load_more_button.click()
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews = soup.find_all('section', {'class': 'pr-review-display pr-rd-display-desktop'})
        # add a delay to allow the new reviews to load
        time.sleep(1)
    except:
        # "Load More" button not found or no more reviews to load
            break
    

    
         

for review in reviews:
    reviewData = {}
    reviewData['title'] = review.find_element_by_xpath('//*[@id="pr-rd-review-headline-415660006"]').strip()
    reviewData['author'] = review.find_element_by_xpath('//*[@id="pr-review-display"]/div[1]/section[1]/div/div/p[2]/span/span[2]').strip()
    reviewData['rating'] = review.find_element_by_xpath('//*[@id="pr-review-display"]/div[1]/header/div/div/div/div[2]').strip()
    reviewData['text'] = review.find_element_by_xpath('//*[@id="pr-review-display"]/div[1]/section[1]/p[2]').strip()
    reviews.append(reviewData)

# write reviews to a JSON file
with open('reviews.json', 'w') as f:
    json.dump(reviews, f)        


driver.quit()

