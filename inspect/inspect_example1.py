import inspect
import copy

print(inspect.getmembers(copy, inspect.isclass))
# [('Error', <class 'copy.Error'>), ('error', <class 'copy.Error'>)]

# 活動中のすべてのオブジェクトを取得する
# https://docs.python.org/ja/3/library/inspect.html

# モジュール内にある全てのメンバ変数を取得できる
