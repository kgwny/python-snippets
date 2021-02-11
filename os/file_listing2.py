from pathlib import Path

# Pathオブジェクト
# ここでは1つ上のディレクトリを基準に作る
path = Path('..')
file_list = sorted(path.glob('**/*.py'))

# 再帰的にサブディレクトリ内の'.py'ファイルを全て列挙する
for p in file_list:
    print(p)

print('ファイル総数:', len(file_list))
