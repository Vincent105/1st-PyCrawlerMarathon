#   搜尋文檔
from bs4 import NavigableString
from bs4 import BeautifulSoup
import re

html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

# use regular expression
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.find_all('b', encoding='utf-8'))

for tag in soup.find_all(re.compile("^b")):  # 僅搜尋b開頭
    print(tag.name)

for tag in soup.find_all(re.compile("t")):   # 搜尋只要包含t
    print(tag.name)

# use list
print(soup.find_all(["a", "b"]))

for tag in soup.find_all(True):
    print(tag.name)

# define a method to find tag


def has_class_but_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


print(soup.find_all(has_class_but_no_id))

# 找出 href 不符合re規則的標籤


def not_lacie(href):
    return href and not re.compile("lacie").search(href)


print(soup.find_all(href=not_lacie))

# 透過


def surrounded_by_strings(tag):
    return (isinstance(tag.next_element, NavigableString)
            and isinstance(tag.previous_element, NavigableString))


for tag in soup.find_all(surrounded_by_strings):
    print(tag.name)

# find_all
print(soup.find_all('title'))
print(soup.find_all('p', "title"))
print(soup.find_all('a'))
print(soup.find_all(id='link2'))

print(soup.find(string=re.compile("sisters")))
print(soup.find_all(href=re.compile("lacie")))
print(soup.find_all(id=True))

# use 2 attrs to search the target
print(soup.find_all(href=re.compile("tillie"), id=True))

# use css selector to search the target
print(soup.find_all('a', class_='sister'))
print(soup.find_all(re.compile("itl")))


def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6


print(soup.find_all(class_=has_six_characters))

css_soup = BeautifulSoup('<p class="body strikeout"></p>')
print(css_soup.find_all('p', class_='strikeout'))
print(css_soup.find_all('p', class_='body'))
print(css_soup.find_all('p', class_='body strikeout'))

print(soup.find_all("a", attrs={"class": 'sister'}))

# string
print(soup.find_all(string="Elsie"))
print(soup.find_all(string=["Tillie", "Elsie", "Lacie"]))
print(soup.find_all(string=re.compile("Dormouse")))


def is_the_only_string_with_a_tag(s):
    """Return True if this string is the only child of its parent tag."""
    return (s == s.parent.string)


print(soup.find_all(string=is_the_only_string_with_a_tag))
print(soup.find_all("a", string='Elsie'))
print(soup.find_all("a", limit=2))
print(soup.html.find_all("title", recursive=False))  # 只能查詢直接子節點
print(soup.html.find_all("title", recursive=True))   # 可以查詢子孫節點

print(soup.title.find_all(string=True))
print(soup.title(string=True))

print(soup.head.title)

# find_parents() find_parent
a_string = soup.find(string='Lacie')
print(a_string)
print(a_string.find_parents("a"))
print("\n")
print(a_string.find_parents("p"))
