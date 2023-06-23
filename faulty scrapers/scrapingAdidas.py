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

url = 'https://www.adidas.nl/superstar-schoenen/EG4958.html'
driver.get(url)
sleep(randint(2,3))



next_button =  driver.find_element(By.XPATH,  '//*[@id="navigation-target-reviews"]/div/button/div[2]')
next_button.click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.find_all('div', {'class': 'reviews___10WEp'})


while True:
    try:
        
        load_more_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="bazaarvoice-container"]/div/div[1]/button')))
        load_more_button.click()
        
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews.extend(soup.find_all('div', {'class': 'reviews___10WEp'}))

        time.sleep(1)
    except:
        
            break
    
    
    
         
reviews_data = []

for review in reviews:
    review_data = {}
    review_data['title'] = review.find('div', {'class': '//*[@id="bazaarvoice-container"]/article[5]/div[1]/strong'}).text.strip()
    review_data['text'] = review.find('div', {'class': '//*[@id="bazaarvoice-container"]/article[6]/div[3]/div[1]'}).text.strip()
    reviews_data.append(review_data)
    


with open('reviews.json', 'w') as f:
    json.dump(reviews_data, f)        

print(reviews_data)
driver.quit()