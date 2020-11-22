from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("start tag:", tag)

    def handle_endtag(self, tag):
        print("end tag:", tag)

    def handle_data(self, data):
        print("data:", data)

parser = MyHTMLParser()
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>header</h1></body></html>')
