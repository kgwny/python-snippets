from flask import Flask, render_template, make_response, request
import os
import json
import datetime
import socket

app = Flask(__name__)

@app.route('/resp')
def resp():
    # 30 sec
    max_age = 30
    expires = int(datetime.datetime.now().timestamp()) + max_age
    response = make_response(render_template("cookie2.html"))
    user_info = "kiteretsu100"
    response.set_cookie('user_info', user_info)
    # host name
    print(socket.gethostname())
    return response

@app.route('/view')
def view():
    user_info = request.cookies.get('user_info')
    return render_template("view2.html", user_info = user_info)

app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
