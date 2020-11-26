import re
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.url = ''
        self.found_headline = False
        self.headline_texts = []

    # 開始タグに含まれる要素の値を抽出する
    def handle_starttag(self, tag, attrs):
        if re.match('^h[1-9]$', tag):
            self.found_headline = True
        if tag == 'a':
            attrs = dict(attrs)
            if 'href' in attrs:
                self.url = attrs['href']
                self.found_headline = True

    # タグに括られた値を抽出する
    def handle_data(self, data):
        if self.found_headline:
            if self.url:
                self.headline_texts.append(self.url)
            self.headline_texts.append(data)
            self.found_headline = False

parser = MyHTMLParser()
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>header</h1><a href="http://example.com">example</a></body></html>')
print(parser.headline_texts)
