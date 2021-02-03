import requests
from bs4 import BeautifulSoup

site = requests.get('https://www.google.com')

data = BeautifulSoup(site.text, 'html.parser')

# titleタグを抽出する
print('data.title =', data.title)

# titleのみ抽出する
print('data.title.text =', data.title.text)
