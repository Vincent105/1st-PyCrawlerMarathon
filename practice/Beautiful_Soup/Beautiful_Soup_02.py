# 對象的種類

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b

# name
print(type(tag))
print(tag.name)

# attributes
print(tag['class'])
print(tag.attrs)

# 多值屬性
css_soup = BeautifulSoup('<p class="body strikeout"></p>', 'lxml')
print(css_soup.p['class'])

css_soup = BeautifulSoup('<p class="body"></p>', 'lxml')
print(css_soup.p['class'])

id_soup = BeautifulSoup('<p id="my id"></p>', 'lxml')
print(id_soup.p['id'])

rel_soup = BeautifulSoup(
    '<p>Back to the <a rel="index">homepage</a></p>', 'lxml')
print(rel_soup.a['rel'])

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)

xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])

# bs4.element.NavigableString
print(tag.string)
print(type(tag.string))

unicode_string = str(tag.string)
print(unicode_string)
print(type(unicode_string))
tag.string.replace_with("NO")
print(tag)

print(soup.name)