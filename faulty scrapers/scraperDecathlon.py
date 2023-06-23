import csv
# from imp import reload
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time


# webdriver setup
options = Options()
# options.add_argument('--headless')
driver = webdriver.Chrome(options = options) 

# gegevens ophalen van url
url = 'https://www.decathlon.nl/r/halfhoge-waterdichte-bergwandelschoenen-voor-heren-mh500-grijs/_/R-p-X8493840?mc=8493840&c=GRIJS'
driver.get(url)

csv_file = open('review.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Title','Author','Rating','Date','Text'])

# scrape de reviews op de eerste pagina
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
reviews = soup.find_all('div', {'class': 'review-list svelte-1peidim'})
# with open('x.html', 'w', encoding='utf-8') as f:
#     f.write(str(html_source))



# loop door de overige pagina's 
for i in range(1, 346):
    try:
        # wacht totdat de volgende pagina button geladen is
        next_button =  driver.find_element(By.XPATH,  '//*[@id="reviews-floor"]/div/section/nav/button['+str(i)+']')
        
        next_button.click()

    except:
        break
    
    # wachten totdat de reviews geladen zijn
    time.sleep(2)
    
    # scrape reviews op huidige pagina
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    reviews.extend(soup.find_all('div', {'class': 'answer-body svelte-1v1nczs'}))

# print alle scraped reviews uit
for review in reviews:
        title = review.find('h3',{'class' : 'review-title vtmn-typo_title-5 svelte-ahfwwb'})
        author = review.find('strong', {'class': 'svelte-1qnyj4l'})
        rating = review.find('span', {'class': 'vtmn-rating_comment--primary'})
        date = review.find('time', {'class': 'svelte-ahfwwb'})
        text = review.find('p', {'class': 'answer-body svelte-1v1nczs'})

        csv_writer.writerow([title, author, rating, date, text])

# close de csv
csv_file.close()

# close de webdriver
driver.quit()