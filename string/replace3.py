import re

html_content = '''
## Python-Markdownを使用してMarkdownをHTMLへ変換する

### Python-Markdownの概要
「Python-Markdown」はPythonでMarkdownを扱うためのライブラリ。<br>

<https://github.com/Python-Markdown/markdown>

インストールするには下記コマンドを実行する。

    $ pip install markdown

<br>

### 見出し
書式：文字列の先頭に半角シャープを1つ〜6つ付与する。シャープの数で見出しの大きさが変わる。
'''

html_content = re.sub('<.*?>|\n|#| ', '', html_content)
html_content = html_content[0:120]
meta_description = '<meta name="description" content="{}">'.format(html_content)
print(meta_description)
