# list(配列)
tmp_list = []
tmp_list.append("a")
tmp_list.append("b")
tmp_list.append("c")
tmp_list.append("a")
print(tmp_list)
# ['a', 'b', 'c', 'a']

# list(配列)をset(集合)へ変換する
tmp_set = set(tmp_list)
print(tmp_set)
# {'a', 'c', 'b'}

# set(集合)をlist(配列)へ変換する
tmp_set_list = list(tmp_set)
print(tmp_set_list)
# ['b', 'a', 'c'] ただし、並び順は実行する都度異なる

# list(配列)の中身を昇順に並び替える
tmp_set_list = sorted(tmp_set_list)
print(tmp_set_list)
# ['a', 'b', 'c']
