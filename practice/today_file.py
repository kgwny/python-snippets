from datetime import datetime 

today = datetime.now().strftime("%Y%m%d") 
# YYYYMMDD形式で日付を取得する

# 連結演算子を使用
file_1 = "file_" + today + ".txt"
print(file_1)

# %構文を使用
file_2 = "file_%s.txt" % today
print(file_2)

# formatメソッドを使用
file_3 = "file_{}.txt".format(today)
print(file_3)
