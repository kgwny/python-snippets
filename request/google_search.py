import requests

# google search
url = "https://www.google.co.jp/search"

params = {
    "q": "天気",
    "tbm": "nws"
}

# get response
r = requests.get(url, params=params)

print(r.status_code)
print(r.headers["content-type"])
print(r.encoding)
print(r.text)
