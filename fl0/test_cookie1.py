from flask import Flask, render_template, make_response, request
import os
import json
import datetime

app = Flask(__name__)

@app.route('/resp')
def resp():
    # 30 sec
    max_age = 30
    expires = int(datetime.datetime.now().timestamp()) + max_age
    response = make_response(render_template("cookie.html"))
    # cookieに格納するデータ
    user_info = {'id':'123', 'password':'user_password'}
    response.set_cookie("user_info", value=json.dumps(user_info), expires=expires)
    return response

@app.route('/view')
def view():
    user_info = request.cookies.get('user_info')
    if user_info is not None:
        user_info = json.loads(user_info)
    return render_template("view.html", user_info = user_info)

app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
