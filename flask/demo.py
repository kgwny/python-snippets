from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 下記URLへアクセスすると、"Hello, world!"が表示される
# http://localhost:5000/
