
out_list = [1, 2, 3, 4, 5]

file_path = 'tmp.txt'

# リストから取得した値に改行コードを付けてファイルに書き込む
with open(file_path, mode='w') as f:
    [f.write(str(s) + '\n') for s in out_list]

# ファイルからリストを取り出してリスト内の全要素に付与された改行コードを削る
with open(file_path) as f:
    in_list = [s.strip() for s in f.readlines()]
    print(in_list)
