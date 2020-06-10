import requests

url = "https://www.google.co.jp/search"

params = {
    "q": "天気",
    "tbm": "nws"
}

response = requests.get(url, params=params)

print(response)
