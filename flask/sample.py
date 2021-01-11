from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return '<html><body><h1>Hello World Wide Web</h1></body></html>'
 
if __name__ == '__main__':
    app.run()

# 下記URLへアクセスすると、"Hello World Wide Web"が表示される
# http://localhost:5000/
