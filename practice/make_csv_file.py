import datetime
import csv

# 日時の取得
now = datetime.datetime.now()

# ディレクトリを指定してファイルを出力
# ファイル名の形式は、log_yyyymmdd_hhmmss.csv
filename = './tmp/log_' + now.strftime('%Y%m%d_%H%M%S') + '.csv'

# ヘッダ行
with open(filename, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['x','y','z'])

x,y,z = 0,0,0

while(1):
    # なんらかの処理
    x += 1
    y += 2
    z += 3

    # filenameを作成したファイル名に合わせる
    # writer.writerowを使用することで、listを１行ずつcsvに書き込む
    with open(filename, 'a', newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x, y, z])

    # 処理が終わったらbreak
    break
