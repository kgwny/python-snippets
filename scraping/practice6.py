from bs4 import BeautifulSoup

html = '''
<a href="http://example.com">リンク文字列1</a>
<a href="http://example.com">リンク文字列2</a>
<div id="column1" class="class1">div1</div>
<div id="column2" class="class2">div2</div>
'''

soup = BeautifulSoup(html, 'html.parser')
print(soup)

# href を取得する
print(soup.find('a')['href'])

# リンクのテキストを取得する
print(soup.find('a').get_text())

# 戻り値はジェネレーターで取得する
print(soup.find('div').stripped_strings)

# 対象をすべて取得する
print([value.stripped_strings for value in soup.find_all('div')])
