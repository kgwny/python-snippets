import os.path
import pathlib

# 実行するファイルの格納パスを取得する

# os.path
# 相対パスの取得
print(os.path.dirname(__file__))

# 絶対パスの取得
print(os.path.dirname(os.path.abspath(__file__)))

# pathlib
# 相対パスの取得
print(pathlib.Path(__file__).parent)

# 絶対パスの取得
print(pathlib.Path(__file__).parent.resolve())
