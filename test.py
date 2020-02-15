from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd

url = "https://www.cupoy.com/newsfeed/topicgrp/life_tw"

browser = webdriver.Chrome(
    executable_path='E:\Project\\1st-PyCrawlerMarathon\chromedriver\chromedriver.exe')
browser.get(url)
time.sleep(5)

article_count = 1
target_count = 35
article_url = []
article_content = {}

keepGoing = True

while keepGoing:
    html = browser.page_source
    soup = BeautifulSoup(html, "lxml")

    news_block = soup.find_all('div', class_='sc-eEieub sc-iuDHTM ibJqYc')

    for news_item in news_block:
        url = news_item.find('a', class_='sc-RbTVP sc-kEmuub eSJXii').get("href")
        article_content.setdefault(article_count, {})

        if url not in article_url and article_count < target_count:
            article_url.append(url)
            article_content[article_count]['標題'] = news_item.find('h6').text
            article_content[article_count]['分類'] = news_item.find('div', class_='sc-gacfCG bPSpUf').string
            article_content[article_count]['摘要'] = news_item.find('p', class_='sc-FQuPU sc-ciodno bvnzOw').string
            article_content[article_count]['連結'] = url
            article_count += 1
        elif url not in article_url and article_count == target_count:    
            article_content[article_count]['標題'] = news_item.find('h6').text
            article_content[article_count]['分類'] = news_item.find('div', class_='sc-gacfCG bPSpUf').string
            article_content[article_count]['摘要'] = news_item.find('p', class_='sc-FQuPU sc-ciodno bvnzOw').string
            article_content[article_count]['連結'] = url               
            keepGoing = False

    time.sleep(2)
    browser.execute_script("window.scrollBy(0,10000)")

# print(article_content)

frame = pd.DataFrame(article_content)
print(frame.T)