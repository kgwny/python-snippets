import os

# 文字列表現はシングルクォート、ダブルクォートどちらを用いても構わない
# 個人的にはダブルクォート推し

print("message = " + "hoge")

print("current work dir = ", os.getcwd())

# 実行ファイル名が出力される
print("running file = ", __file__)
