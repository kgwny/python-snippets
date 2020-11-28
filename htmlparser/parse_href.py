import re
from html.parser import HTMLParser

class TestParser(HTMLParser):
 
    def __init__(self):
        HTMLParser.__init__(self)
        self.url = ""
 
    def handle_starttag(self, tag, attrs):
        # aタグのhref属性に設定されている値を取り出す
        if tag == "a":
            attrs = dict(attrs)
            if 'href' in attrs:
                self.url = attrs['href']
 
    def handle_endtag(self, tag):
        if self.url and re.match('^http', self.url):
            print(self.url)
            self.url = ""

parser = TestParser()
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>header</h1><a href="http://example.com">example</a></body></html>')
# http://example.com
