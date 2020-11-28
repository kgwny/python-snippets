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
# start tag: html
# start tag: head
# start tag: title
# data: test
# end tag: title
# end tag: head
# start tag: body
# start tag: h1
# data: header
# end tag: h1
# end tag: body
# end tag: html
