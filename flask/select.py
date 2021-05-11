from flask import Flask
import mysql.connector

# DB接続情報
def conn_db():
    conn = mysql.connector.connect(
        host = 'localhost',
        user = 'localadmin',
        passwd = 'passwd',
        db = 'sqmple'
    )
    return conn

# 本体
sql = 'SELECT * FROM sample'

try:
    conn = conn_db()    # DB接続
    cursor = conn.cursor()  # カーソル取得
    cursor.execute(sql)     # select文発行
    rows = cursor.fetchall()    # selectの結果をタプルへ格納する
except(mysql.connector.errors.ProgrammingError) as e:
    print('error detected')
    print(e)

print('result')
for row in rows:
    print(row[0], row[1], row[2])

# SQLの実行結果を全件取得してタプルへ格納してprint
# 1件ずつ受けたい場合は、cursor.fetchone()を使う
