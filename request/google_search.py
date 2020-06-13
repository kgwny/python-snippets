import requests

# google search
url = 'https://www.google.co.jp/search'

params = {
    'q': '天気',
    'tbm': 'nws'
}

# get response
res = requests.get(url, params=params)

print(res.status_code)
print(res.headers['content-type'])
print(res.encoding)
print(res.text)
