import scrapy
from bs4 import BeautifulSoup

class Parser(object):
    def __init__(self, html: str):
        self._soup = BeautifulSoup(html, 'html.parser')

    def parse_title(self):
        return self._soup.find('title').get_text(strip=True)

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        # レスポンスから Parser オブジェクトを生成する
        parser = Parser(response.text)
        title_text = parser.parse_title()
