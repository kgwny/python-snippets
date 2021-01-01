import os
import shutil

# 指定したディレクトリを削除する
target_dir = './output'

if os.path.exists(target_dir):
    # os.removeを実行するとパーミッションエラーとなる
    # os.remove(target_dir)
    shutil.rmtree(target_dir)
