import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/explore'

# 加上 Header 即可取回正常資料
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

r = requests.get(url, headers=headers)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text.replace(r'\u002F', '/').replace(r'\u003C', '<').replace(r'\u003E', '>'),'html.parser')
 
print(soup.prettify()) 

a_tags = soup.find_all('a',class_='ExploreRoundtableCard-title')
for tag in a_tags:
  print(tag.string)