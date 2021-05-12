from flask import Flask, render_template, make_response, request

# ルーティングとパラメータ
@app.route("/start", methods=["GET", "POST"])
def start():
    if request.method == "POST":
        # POSTされたformから取得
        user_id = request.form["user_id"]
    else:
        # GETのURLから取得
        user_id = request.args.get("user_id")

@app.route("/start_2/<user_id>", method=["GET"])
def start_2():
    # /start_2/1 にアクセスされると user_id に1を格納  


# レスポンス
@app.route("/")
def index():
    response = make_response(render_template("index.html"))
    return response

@app.route("/json")
def get_json():
    response = make_response(jsonify({"result": 1}))
    return respnose

app.run(debug=True, host=os.getenv('APP_ADDRESS', 'localhost'), port=8001)
