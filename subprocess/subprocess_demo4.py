import subprocess
import sys

cp = subprocess.run(['wc'], input='ika tako', encoding='UTF-8')
print(cp)
#      0       2       8

# wcコマンドはテキストファイルの行数、単語数（word count）、文字数を数える
# 単語は空白や改行文字で区切られたものを数える
