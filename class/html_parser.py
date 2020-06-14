from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('タグ開始:', tag)

    def handle_endtag(self, tag):
        print('タグ終了:', tag)

    def handle_data(self, data):
        print('その他データ:', data)

parser = MyHTMLParser()
parser.feed('<title>タイトル</title>'
            '<h1>見出し</h1>')
#タグ開始: title
#その他データ : タイトル
#タグ終了 : title
#タグ開始: h1
#その他データ : 見出し
#タグ終了 : h1
