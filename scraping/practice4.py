import requests
import scrapy
from bs4 import BeautifulSoup

# 要インストール
# $ pip install scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # レスポンスから BeautifulSoup オブジェクトを生成する
        soup = BeautifulSoup(response.text, 'html.parser')

        # 通常の Beautiful Soup と同じように使うことができる
        title_text = soup.find('title').get_text(strip=True)
        print(title_text)

# スクレイピング対象の URL にリクエストを送り HTML を取得する
res = requests.get('http://quotes.toscrape.com/')

q = QuotesSpider()
q.parse(res)
