import os

# ディレクトリ一覧の取得
path = './'
dir_list = os.listdir(path)
dirs = [f for f in dir_list if os.path.isdir(os.path.join(path, f))]
print('ディレクトリ一覧:', dirs)
