import requests
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Origin':'https://www.591.com.tw',
    
    }
r = requests.get('https://www.591.com.tw/', headers=headers)
response = r.text

print(response)
