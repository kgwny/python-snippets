try:
    # エラーではないが成立しない記述
    c = str[0]
except:
    # 例外が発生した場合
    print('Exception')
else:
    # 例外が発生しなかった場合
    print('Else')
finally:
    # 常時実行される
    print('Finally')
