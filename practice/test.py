import requests
from collections import Counter
from bs4 import BeautifulSoup

url = 'https://www.ettoday.net/news/news-list.htm'
r = requests.get(url)

soup = BeautifulSoup(r.text, "html.parser")
articles = {}
count = 0

for d in soup.find(class_="part_list_2").find_all('h3'):
    # print(d.find(class_="date").text, d.find_all('em')[-1].text , d.find_all('a')[-1].text)

    articles[count] = d.find_all("em")[-1].text
    count += 1
# print(articles)

max_count_tag = Counter(articles.values())
print(max_count_tag.most_common(1)[
      0][0], "類別的文章最多,合計有", max_count_tag.most_common(1)[0][1], "篇")
