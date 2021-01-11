from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hello World!"
    return name

@app.route('/awesome')
def awesome():
    name = "Awesome!"
    return name

@app.route('/great')
def great():
    name = "Great!"
    return name

if __name__ == "__main__":
    app.run(debug=True)

# 下記URLへアクセスすると、"Hello world!"が表示される
# http://localhost:5000/

# 下記URLへアクセスすると、"Awesome!"が表示される
# http://localhost:5000/awesome

# 下記URLへアクセスすると、"Great!"が表示される
# http://localhost:5000/great
