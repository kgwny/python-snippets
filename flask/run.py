# Webサーバを立ち上げる際に実行するファイルです。
from app.app import app

if __name__ == "__main__":
    app.run()

# 起動後に下記URLへアクセスする
# http://127.0.0.1:5000/
# Hello World

# http://127.0.0.1:5000/index
