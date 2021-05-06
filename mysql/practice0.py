# 接続確認
conn.is_connected()  #=> Bool

# コネクションを張りっぱなしにしていると、いつの間にか接続が切れてしまうことがある。
# これを回避するためには定期的に ping を送り、接続できていなければ再接続するようにしておく。
conn.ping(reconnect=True)

# クエリ実行
# 標準の SQLite コネクタ などと同様に、カーソルオブジェクトを作成し execute メソッドでクエリを実行する。
cur = conn.cursor()

# 取得 (SELECT)
# クエリを実行した後に fetchone / fetchmany / fetchall メソッドでレコードを取得できる。
cur.execute('SELECT * FROM users')
cur.fetchall()  #=> [(1, 'foo'), (2, 'bar')]

# プリペアードステートメントも利用できる。
cur.execute('SELECT * FROM users WHERE id = %s', [1])
cur.statement  #=> 'SELECT * FROM users WHERE id = 1'
cur.fetchone()  #=> (1, 'foo')

# 更新 (INSERT / UPDATE / DELETE)
# クエリ実行後に conn.commit() でコミットされる。
try:
    cur.execute('INSERT INTO users (name) VALUES (%s)', ['foo'])
    conn.commit()
except:
    conn.rollback()
    raise

# 結果をディクショナリとして取得
# カーソルオブジェクト作成時に dictionary オプションを渡すとクエリ実行結果をディクショナリとして取得できる。
cur = conn.cursor(dictionary=True)
cur.fetchall()  #=> [{'id': 1, 'name': 'foo'}, {'id': 2, 'name': 'bar'}]
