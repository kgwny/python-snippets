import os

# ファイル一覧の取得
path = './'
file_list = os.listdir(path)
files = [f for f in file_list if os.path.isfile(os.path.join(path, f))]
print('ファイル一覧:', files)

# mdファイル一覧の取得
path = './'
file_list = os.listdir(path)
files = [f for f in file_list if os.path.isfile(os.path.join(path, f)) and f.endswith('.md')]
print('mdファイル一覧:', files)

for s in files:
    print('ファイル名:', s)
    print('拡張子抜きのファイル名:', s[0:len(s)-3])
