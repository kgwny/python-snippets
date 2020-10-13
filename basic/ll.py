import os, os.path

# ファイルとサブディレクトリのパスを表示する
path = '/Users/xxx'
for root, dirs, files in os.walk(path):
    for file in files:
        print(os.path.join(root, file))
