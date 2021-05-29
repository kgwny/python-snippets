# Ternary Conditionals（条件式）
condition = True

if condition:
    x = 1
else:
    x = 0

print(x)

# ワンライナー
x = 1 if condition else 0


# Underscore Placeholders：アンダースコアで強調させる
# 数値は_区切りで表現することができる

num1 = 10000000000

num1 = 10_000_000_000

print(f'{num1:,}')


# Context Managers:コンテキストマネージャ
# コンテキストマネージャとは、with文の実行時にruntime contextを定義するオブジェクトのことです
# ＊runtime context とは
# __enter__()呼び出しで組み立てられて、__exit__()呼び出しで取り壊される環境のこと

import os
path = os.getcwd() + '/examples/test.txt'
f = open(path, 'r', encoding="utf-8")
file_contents = f.read()
f.close()

words = file_contents.split('\n')
word_count = len(words)
print(word_count)
