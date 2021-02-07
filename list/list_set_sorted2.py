# list(配列)
tmp_list = []
tmp_list.append("a")
tmp_list.append("b")
tmp_list.append("c")
tmp_list.append("a")
print(tmp_list)
# ['a', 'b', 'c', 'a']

# list(配列)をset(集合)へ変換したあと、list(配列)へ再度変換する
# さらに昇順に並び替える
tmp_set_list = sorted(list(set(tmp_list)))
print(tmp_set_list)
# ['a', 'b', 'c']
