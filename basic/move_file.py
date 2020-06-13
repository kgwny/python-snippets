import os
import pathlib
import shutil

# ファイルを作成する
# ディレクトリを作成する
# ファイルをディレクトリ配下へ移動する

target_file = 'blank.txt'

# create file
target_path = pathlib.Path(target_file)
target_path.touch()

target_dir = 'tmp'

# create dir
os.makedirs(target_dir, exist_ok=True)

shutil.move(target_file, target_dir)

if os.path.exists(target_dir + '/' + target_file):
    print('file moved')
