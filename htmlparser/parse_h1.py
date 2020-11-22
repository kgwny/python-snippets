from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):

    def __init__(self):
        super().__init__()
        self.found_headline = False
        self.headline_texts = []

    def handle_starttag(self, tag, attrs):
        if tag == "h1":
            self.found_headline = True

    def handle_data(self, data):
        if self.found_headline:
            self.headline_texts.append(data)
            self.found_headline = False

parser = MyHTMLParser()
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>header</h1></body></html>')
print(parser.headline_texts[0])
