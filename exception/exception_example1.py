# try:
#     例外が発生するかもしれない処理
# except 捕捉する例外ハンドラ as 識別子:
#     発生した例外に対する処理
# else:
#     例外が発生しなかった場合の処理
# finally:
#     例外発生の有無に関わらず実行する処理

try:
    lis = []
    print(lis[0])
except:
    print('Error detected')
