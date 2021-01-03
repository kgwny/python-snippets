import requests
from bs4 import BeautifulSoup

# 要インストール
# $ pip install requests
# $ pip install beautifulsoup4

# クローラーの例

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('https://www.yahoo.co.jp/')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# title タグの文字列を取得する
title_text = soup.find('title').get_text()
print(title_text)

# ページに含まれるリンクを全て取得する
links = [url.get('href') for url in soup.find_all('a')]
print(links)

# class が quote の div 要素を全て取得する
quote_elms = soup.find_all('div', {'class': 'quote'})
print(len(quote_elms))
