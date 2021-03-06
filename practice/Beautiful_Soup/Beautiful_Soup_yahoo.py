import requests
import re
from bs4 import BeautifulSoup

url = 'https://www.yahoo.com'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}

r = requests.get(url, headers=headers)
r.encoding = 'utf-8'

soup = BeautifulSoup(r.text, 'html.parser')
soup = soup.body
''' test_02
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p)
print(soup.p['class'])
print(soup.a)
print(soup.find_all('a'))
print(soup.find(href="https://tw.mail.yahoo.com"))

for link in soup.find_all('a'):
    print(link.get('href'))

test = soup.find(class_="Pos-r NoTextDecoration i13n rapidnofollow")
print(test)
print(test.name)
print(test['class'])
print(test.attrs)

css_soup = BeautifulSoup(r.text, 'lxml')
print(css_soup.p['class'])
print(css_soup.a['href'])
'''

''' test_03
print(soup.head)
print(soup.title)
print(soup.meta)
print(soup.find_all('a'))

#   利用.contents 將子節點以列表輸出
title_tag = soup.title
print(title_tag)
print(title_tag.contents)

for child in title_tag.children:
    print(child)

for string in soup.stripped_strings:
    print(repr(string))

sibling = soup.div

print(sibling)
print(sibling.next_sibling)
print(sibling.previous_sibling)

for tag in soup.find_all(re.compile("^b")):  # 僅搜尋b開頭
    print(tag.name)

for tag in soup.find_all(re.compile("t")):   # 搜尋只要包含t
    print(tag.name)

# use list
print(soup.find_all(["a", "b"]))

for tag in soup.find_all(True):
    print(tag.name)
print(soup.find_all('title'))
print(soup.find_all('p', "title"))

print(soup.find_all('span', class_='Cur-p D-ib Py-8 C-blue MouseOver-TextDecoration'))
'''

print(soup.find(href=re.compile("tw.news.yahoo.com")))
print(soup.find_all("a", limit=4))

a_string = soup.find(string='新聞')
print(a_string.find_parents("a"))
a_string = soup.find(string='股市')
print(a_string.find_parents("a"))
print(a_string.find_parents("li"))


