str_1 = 'hogehoge'
list_1 = [100, 200, 300]
list_2 = [100, 200, 300]
  
print(list_1 == list_2)
# True

print(list_1 is list_2)
# False

print(id(list_1))
# 実行環境により異なる番号が出力される

print(id(list_1) == id(list_1))
# True

print(list_1 is list_1)
# True

print(str_1 == 'hogehoge')
# True

print(str_1 is 'hogehoge')
# True
