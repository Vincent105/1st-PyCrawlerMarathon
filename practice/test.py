import requests
import collections
from bs4 import BeautifulSoup

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text.replace(u'\u3000', '　'), "html.parser")
articles = {}
count = 0

for d in soup.find(class_="part_list_2").find_all('h3'):
    # print(d.find(class_="date").text, d.find_all('em')[-1].text , d.find_all('a')[-1].text)

    articles[count] = ({'date': d.find(class_="date").text,
                        'title': d.find_all('a')[-1].text.replace(u'\u3000', '　'),
                        'tag': d.find_all("em")[-1].text})
    count += 1
print(articles)
