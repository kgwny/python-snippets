import requests
from bs4 import BeautifulSoup

# 要インストール
# $ pip install requests
# $ pip install beautifulsoup4

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('http://quotes.toscrape.com/')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

# CSS セレクターを使って id を全て取得する
ids = [n.get_text() for n in soup.select('div.quote small.author')]
print(ids)

tag_items = soup.select('h2:contains("Top Ten tags") ~ span')
print([t.get_text(strip=True) for t in tag_items])
