import urllib.parse

# base_urlのページ内に記述されている相対URLから絶対URLを導き出す

base_url = 'http://www.example.com/foo/bar.html'
link_url1 = '../hoge/fuga.html'
link_url2 = './piyo.html'

full_url1 = urllib.parse.urljoin(base_url, link_url1)
print(full_url1)
# http://www.example.com/hoge/fuga.html

full_url2 = urllib.parse.urljoin(base_url, link_url2)
print(full_url2)
# http://www.example.com/foo/piyo.html
