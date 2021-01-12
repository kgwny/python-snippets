# 必要なモジュールの取り込み
from flask import Flask

# Flaskオブジェクトの生成
app = Flask(__name__)

# ルート( / )へアクセスがあった時の処理を記述
@app.route("/")
def root():
    return "Hello"

# サーバーを起動
if __name__ == "__main__":
    app.run(debug=True, port=8888)

# 下記URLへアクセスすると、"Hello"が表示される
# http://localhost:8888/
