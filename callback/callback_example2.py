def handler(func, *args):
    return func(*args)

def print_msg1(msg1):
    print('%s' % msg1)

def print_msg2(msg1, msg2):
    print('%s, %s' % (msg1, msg2))

if __name__ == '__main__':

   # コールバック関数の代入
   callback1 = print_msg1
   # ハンドラーの実行 : コールバック関数の呼び出し
   handler(callback1, 'msg1')

   # コールバック関数の代入
   callback2 = print_msg2
   # ハンドラーの実行 : コールバック関数の呼び出し
   handler(callback2, 'msg1', 'msg2')
