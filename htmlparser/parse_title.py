from html.parser import HTMLParser
 
class TestParser(HTMLParser):
 
    def __init__(self):
        HTMLParser.__init__(self)
        self.flag = False
 
    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self.flag = True
 
    def handle_data(self, data):
        if self.flag:
            print(data)
            self.flag = False

parser = TestParser()
parser.feed('<html><head><title>test</title></head>'
            '<body><h1>header</h1></body></html>')
# test
