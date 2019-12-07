from bs4 import BeautifulSoup

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
soup = BeautifulSoup(html_doc, 'html.parser')
print(soup.head)
print(soup.title)
print(soup.body.b)
print(soup.a)
print(soup.find_all('a'))

#   利用.contents 將子節點以列表輸出
head_tag = soup.head
print(head_tag)
print(head_tag.contents)
title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

for child in title_tag.children:
    print(child)

#   .descendants
for child in head_tag.descendants:
    print(child)

print(len(list(soup.children)))
print(len(list(soup.descendants)))

# .strings 和 stripped_strings
for string in soup.strings:
    print(repr(string))

for string in soup.stripped_strings:
    print(repr(string))

#   .parent
title_tag = soup.title
print(title_tag)
print(title_tag.parent)
print(title_tag.string.parent)
html_tag = soup.html
print(type(html_tag.parent))

#   .parents
link = soup.a
print(link)
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

#   .sibling
sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
print(sibling_soup.prettify())

print(sibling_soup.b.next_sibling)
print(sibling_soup.b.previous_sibling)

print(sibling_soup.c.next_sibling)
print(sibling_soup.c.previous_sibling)

#   .siblings
for sibling in soup.a.next_siblings:
    print(sibling)

for sibling in soup.find(id='link3').previous_siblings:
    print(sibling)
