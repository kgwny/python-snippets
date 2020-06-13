from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(f'')

    def handle_endtag(self, tag):
        print(f'')

    def handle_data(self, data):
        print(f'{data}')

parser = MyHTMLParser()
parser.feed('<html><head><title>天気予報</title></head><body>本日は晴天なり</body></html>')
