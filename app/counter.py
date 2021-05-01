import fcntl

#　カウントファイル
dat = "./dat/count.dat"

#　カウントファイルを開く
fh = open(dat, "r+")

#　ファイルロック
fcntl.flock(fh.fileno(), fcntl.LOCK_EX)

#　カウント読み込み
count = fh.read()

#　文字列を数字に変換
count = int(count)

#　カウントに1加える
count += 1

#　数字を文字列に変換
count = str(count)

# ファイルポインタを先頭に移動
fh.seek(0)

#　カウント書き込み
fh.write(count)

#　ファイルロック解除
fcntl.flock(fh.fileno(), fcntl.LOCK_UN)

#　カウントファイルを閉じる
fh.close()

#　HTML出力
print("Content-type: text/html")
header = """
<html>
<head>
<title>アクセスカウンター</title>
</head>
<body>
"""

content = "あなたは %s 人目の訪問者です。" % count

footer = """</body>
</html>
""" 

print(header + content + footer)
