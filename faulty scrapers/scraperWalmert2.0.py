import os
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup

import time
from time import sleep
from random import randint

chromedriver = "C:\Program Files\Python39\Scripts\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
chromedriver = "C:\Program Files\Python39\Scripts\chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


url = 'https://www.walmart.com/reviews/product/108210308'
driver.get(url)
sleep(randint(2,3))

element = driver.find_element(By.XPATH, "//div[@id='px-captcha']")
action = ActionChains(driver)
click = ActionChains(driver)
frame_x = element.location['x']
frame_y = element.location['y']
x_move = frame_x + element.size['width']*0.5
y_move = frame_y + element.size['height']*0.5
action.move_to_element_with_offset(element, x_move, y_move).click_and_hold().perform()
time.sleep(10)
action.release(element)
action.perform()
time.sleep(0.2)
action.release(element)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.find_all('ul', {'class': 'cc-3 cg-4 pl0 mt4'})

# Open CSV file and create writer object
with open('WalmartReviews.csv', 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write header row to CSV
    csv_writer.writerow(['Title','Author','Rating','Date','Text'])

    for i in range(2+1, 200+1):
        try:
            # Wait until the next page button is loaded
            next_button =  driver.find_element(By.XPATH,'//*[@id="maincontent"]/main/nav/ul/li['+str(i)+']/a')
            next_button.click()

        except:
            break

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        reviews.extend(soup.find_all('ul', {'class': 'cc-3 cg-4 pl0 mt4'}))

        # Process each review and write data to CSV
        for review in reviews:
            try:
                date = review.find('div',{'class' : 'f7 gray'}).text.strip()
            except:
                date = ""

            try:
                author = review.find('div', {'class': 'f6 gray pr2'}).text.strip()
            except:
                author = ""

            try:
                rating = review.find('span', {'class': 'w_iUH7'}).text.strip()
            except:
                rating = ""

            try:
                title = review.find('span', {'class': 'b w_V_DM'}).text.strip()
            except:
                title = ""

            try:
                findText = review.find('span', {'class': 'tl-m db-m'})
                findElementInSpan = findText.find('span')
                text = findElementInSpan.text.strip()
            except:
                text = ""

            csv_writer.writerow([title, author, rating, date, text])

# Close the CSV file
csv_file.close()

driver.quit()