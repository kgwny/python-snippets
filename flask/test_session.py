from flask import Flask, render_template, session
import os

app = Flask(__name__)
# 暗号キー
app.config['SECRET_KEY'] = 'secret_key'

@app.route('/counter')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0
    return render_template("session.html", count = session['counter'])

app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
