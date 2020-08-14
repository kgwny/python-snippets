import os, sys

# 実行中のpyファイル名
print(os.path.basename(__file__))

# pyファイルの格納ディレクトリ名（絶対パス）
print(os.path.dirname(os.path.abspath('__file__')))

# 上と同じ
print(os.path.dirname(os.path.abspath(sys.argv[0])))

# os.path.dirname(__file__) は NG
