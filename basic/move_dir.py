import os
import pathlib
import shutil

# ファイルを作成する
# ディレクトリ(src)を作成する
# ディレクトリ(dist)を作成する
# ファイルをディレクトリ(src)配下へ移動する
# ディレクトリ(src)をディレクトリ(dist)配下へ移動する

src_file = "src.txt"

# create src file
target_path = pathlib.Path(src_file)
target_path.touch()

src_dir = "src"

# create src dir
os.makedirs(src_dir, exist_ok=True)

dist_dir = "dist"

# create dist dir
os.makedirs(dist_dir, exist_ok=True)

# src.txt を src 配下へ移動
shutil.move(src_file, src_dir)

# src を dist 配下へ移動
shutil.move(src_dir, dist_dir)

if os.path.exists(src_dir + "/" + dist_dir + "/" + src_file):
    print("dir moved")
