import mysql.connector
# mysqlの操作
# easy_install mysql-connector-python

try:
    cnn = mysql.connector.connect(host='localhost',
                                  port=3306,
                                  db='Sample001',
                                  user='root',
                                  passwd='root',
                                  charset="cp932")
    cur = cnn.cursor()

    #試験データの整理
    pref_cd = 100
    cur.execute("""DELETE FROM t01prefecture WHERE PREF_CD >= %s""" , (pref_cd,))
    cnn.commit()

    print("SELECT文")
    from_id = 45
    to_id = 999

    # 環境の文字コードにあわせること
    cur.execute("""SELECT PREF_CD,PREF_NAME FROM t01prefecture
                WHERE PREF_CD BETWEEN %s AND %s""" , (from_id, to_id, ))
    rows = cur.fetchall()
    for row in rows:
        print("%d %s" % (row[0], row[1]))

    print("コミット")
    pref_cd = 100
    pref_name = "hoge"
    cur.execute("""INSERT INTO t01prefecture(PREF_CD, PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name))

    pref_cd = 101
    pref_name = "piyo"
    cur.execute("""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name,))
    cnn.commit()

    print("ロールバック")
    pref_cd = 102
    pref_name = "ロールバック"
    cur.execute("""INSERT INTO t01prefecture(PREF_CD,PREF_NAME)
                VALUES (%s, %s)""" , (pref_cd, pref_name,))
    cnn.rollback()

    print("ストアドプロシージャの試験")
    cur.callproc("test_sp", (from_id, to_id))
    for rs in cur.stored_results():
        print("レコードセット...")
        rows = rs.fetchall()
        for row in rows:
            print ("%d %s" % (row[0], row[1]))

    print("ストアドプロシージャの試験複数回")
    cur.callproc("test_sp2", (1, 100))
    for rs in cur.stored_results():
        print("レコードセット...")
        rows = rs.fetchall()
        for row in rows:
            print ("%d %s" % (row[0], row[1]))

    print("ファンクションの試験")
    pref_cd = 100
    cur.execute("""SELECT test_fn(%s)""" , (pref_cd,))
    rows = cur.fetchall()
    for row in rows:
        print("code:%d name:%s" % (pref_cd, row[0]))

    cur.close()
    cnn.close()
except (mysql.connector.errors.ProgrammingError) as e:
    print (e)
