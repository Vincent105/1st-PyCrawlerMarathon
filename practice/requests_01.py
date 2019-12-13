import requests

r = requests.get('https://api.github.com/events')
r = requests.post('http://httpbin.org/post', data={'key': 'value'})
r = requests.delete('http://httpbin.org/delete')
r = requests.head('http://httpbin.org/get')
r = requests.options('http://httpbin.org/get')

# 傳遞url參數
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
r = requests.get('http://httpbin.org/get', params=payload)
print(r.url)

r = requests.get('https://api.github.com/events')
# print(r.text)
print(r.encoding)

