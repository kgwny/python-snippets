import os
import shutil

# 指定したディレクトリをまるごと削除する
target_dir = './output'

if os.path.exists(target_dir):
    # removeを実行するとパーミッションエラーとなる
    # os.remove(target_dir)
    shutil.rmtree(target_dir)
