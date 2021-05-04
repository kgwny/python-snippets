from flask import Flask, render_template, redirect, request, Blueprint, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    # トップページにアクセスされたらindex3.htmlを表示する
    if request.method == "GET":
        return render_template("index3.html")
    elif request.method == "POST":
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        output = firstname + ' ' + lastname
        if firstname and lastname:
            return jsonify({'output':'Your name is ' + output + '.'})
        # return jsonify({'error' : 'Missing data!'})

if __name__ == '__main__':
    app.run(debug=True)

# 下記URLへアクセスする
# http://localhost:5000/
