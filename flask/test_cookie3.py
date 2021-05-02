# no test
# make_responseをインポート
from flask import Flask, make_response

app = Flask(__name__)
@app.route('/')
def index():
    content = "**レスポンス内容**"

    # make_responseでレスポンスオブジェクトを生成する
    response = make_response(content)

    # Cookieの設定を行う
    max_age = 60 * 60 * 24 * 120 # 120 days
    expires = int(datetime.now().timestamp()) + max_age
    response.set_cookie(
        'uid', value="**ユーザーIDなど**", max_age=max_age, 
        expires=expires, path='/', domain=domain, secure=None, httponly=False)

    # レスポンスを返す
    return response

# part2
@app.route("/")
def index():
    max_age = 60 * 60 * 24 # 1 days
    expires = int(datetime.now().timestamp()) + max_age

    user_id = request.cookies.get("user_id", None) # クッキーの取得
    if user_id == None:
        user_id = "aaa"
    # responseの作成
    response = make_response(render_template("index.html")) 
    response.set_cookie("user_id", value=user_id, path=request.path,
                        expires=expires, httponly=True, secure=False)


# part3
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/set')
def set():
    response = make_response('hage-')
    response.set_cookie('cookie_name', 'hige---')
    return response

@app.route('/get')
def get():
    v = request.cookies.get('cookie_name')
    return v

if __name__ == '__main__':
    app.run(debug=True)

