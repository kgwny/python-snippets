# Python + mysql-connector-python の使い方まとめ

import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host='hostname',
    port='3306',
    user='username',
    password='password',
    database='dbname'
)

# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

# テーブル作成
# DB操作用にカーソルを作成
cur = conn.cursor()

# id, name, price を持つテーブルを作成
table = 'test_table'
cur.execute("DROP TABLE IF EXISTS `%s`;", table)
cur.execute(
    """
    CREATE TABLE IF NOT EXISTS `%s` (
    `id` int auto_increment primary key,
    `name` varchar(50) not null,
    `price` int(11) not null
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
    """, table)
)

# データ挿入（INSERT)
cur.execute("INSERT INTO test_table VALUES (1, 'BTC', 10200)")

# プレースホルダを利用して挿入
cur.execute("INSERT INTO test_table VALUES (2, 'ETH', %s)", (5000, ))
cur.execute("INSERT INTO test_table VALUES (%s, %s, %s)", (3 ,'XEM', 2500))
cur.execute("INSERT INTO test_table VALUES (%(id)s, %(name)s, %(price)s)", {'id': 4, 'name': 'XRP', 'price': 1000})

# executemanyで複数データを一度に挿入
records = [
  (5, 'MONA', 3000),
  (6, 'XP', 1000),
]
cur.executemany("INSERT INTO test_table VALUES (%s, %s, %s)", records)


# データ抽出 (SELECT)
cur.execute("SELECT * FROM test_table ORDER BY id ASC")

# 全てのデータを取得
rows = cur.fetchall()

for row in rows:
    print(row)

# 出力結果
"""
(1, 'BTC', 10200)
(2, 'ETH', 5000)
(3 ,'XEM', 2500)
(4, 'XRP', 1000)
(5, 'MONA', 3000)
(6, 'XP', 1000)
"""

# 1件取得
cur.execute("SELECT * FROM test_table WHERE name=%s", ('BTC', ))
print(cur.rowcount)
print(cur.fetchone())

# 出力結果
"""
1
(1, 'BTC', 10200)
"""

# データ更新 (UPDATE)・データ削除 (DELETE)
# UPDATE
cur.execute('UPDATE test_table SET name=%s WHERE id=1', ('ビットコイン',))
cur.execute('UPDATE test_table SET name=%s WHERE id=%s', ('イーサリアム', 2))

# DELETE
cur.execute('DELETE FROM test_table WHERE id = 3')

# コネクションクローズ - DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.close()
