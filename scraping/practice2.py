import requests
from bs4 import BeautifulSoup

# 要インストール
# $ pip install requests
# $ pip install beautifulsoup4

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('http://quotes.toscrape.com/')

# レスポンスの HTML から BeautifulSoup オブジェクトを作る
soup = BeautifulSoup(res.text, 'html.parser')

def get_piyo_text():
    piyo = soup.select_one('div.hoge div.fuga div.piyo')
    if not piyo:
        return None
    return piyo.get_text()
