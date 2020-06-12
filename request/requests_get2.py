import requests

# google search
url = "https://www.google.co.jp/search"

params = {
    "q": "天気",
    "tbm": "nws"
}

# get response
response = requests.get(url, params=params)

print(response)
