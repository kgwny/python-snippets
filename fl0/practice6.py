from flask import Flask
from flask import render_template

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return '<html><body><h1>Hello World Wide Web</h1></body></html>'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404

# サーバーを起動
if __name__ == "__main__":
    app.run()
