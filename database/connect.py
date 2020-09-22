
# mysql-connector-python
# https://pypi.org/project/mysql-connector-python/

# 動作未確認
import mysql.connector

conn = mysql.connector.connect(user='root', password='root', host='localhost', database='test')
cur = conn.cursor()
cur.execute("select * from user;")

for row in cur.fetchall():
    print(row[0], row[1])

cur.close
conn.close
