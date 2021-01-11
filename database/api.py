# -*- coding: utf-8 -*-
from flask import Flask, jsonify, abort, make_response
import peewee
# import json

db = peewee.SqliteDatabase("data.db")

class User(peewee.Model):
    userId = peewee.TextField()
    userCompany = peewee.TextField()
    userDiscountRate = peewee.IntegerField()

    class Meta:
        database = db

api = Flask(__name__)

@api.route('/Users/<string:userId>', methods=['GET'])
def get_user(userId):
    try:
        user = User.get(User.userId == userId)
    except User.DoesNotExist:
        abort(404)

    result = {
        "result":True,
        "data":{
            "userId":user.userId,
            "userCompany":user.userCompany,
            "userDiscountRate":user.userDiscountRate
            }
        }

    return make_response(jsonify(result))
    # Unicodeにしたくない場合は↓
    # return make_response(json.dumps(result, ensure_ascii=False))

@api.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=3000)

# $ curl -i http://0.0.0.0:3000/Users/Usdj7ej1
# HTTP/1.0 200 OK
# Content-Type: text/html; charset=utf-8
# Content-Length: 118
# Server: Werkzeug/0.11.10 Python/3.5.1
# Date: Fri, 27 May 2016 06:29:57 GMT
