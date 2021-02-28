import urllib.request

TARGET_URL = 'https://www.google.com/?hl=ja'

# webページ取得&表示
with urllib.request.urlopen(TARGET_URL) as res:
    html = res.read().decode('utf-8')
    print(html)

# webページ取得&保存
ft = open(r'./tmp.txt', 'wb')
ft.write(urllib.request.urlopen(TARGET_URL).read())
ft.close()
