hoge = 1

try:
    hoge = hoge / 10
except Exception as e:
    print('エラーだよ Exception:', e)
else:
    print('正常終了したよ')
finally:
    print('try文が終了したよ')
