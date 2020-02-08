from requests_html import HTMLSession

session = HTMLSession()
r = session.get('https://python.org/')
# print(r.html.links)
print(r.html.absolute_links)