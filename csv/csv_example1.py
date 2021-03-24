import csv

csv_file = './tmp/test.csv'

with open(csv_file, 'r') as f:
    csv_list = csv.reader(f, delimiter=",", doublequote=True, lineterminator="\n", quotechar='"', skipinitialspace=True)

    # 1行目のCSVヘッダを取得する
    header = next(csv_list)
    print(header)

    # 2行目からのデータ行を取得する
    for row in csv_list:
        print(row)
