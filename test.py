import socket
import urllib.request
import urllib.error

url = 'http://httpbin.org/post'
try:
    response = urllib.request.urlopen(url, timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')
