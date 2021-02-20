# コールバック関数とは
# プログラム中で呼び出し先の関数の実行中に実行されるように、あらかじめ指定しておく関数
# 関数の引数として渡す関数ともいえる

# コールバック関数を呼び出す関数
def handler(func, *args):
    return func(*args)

def say_hello(name):
    print('Hello! {}'.format(name))

if __name__ == '__main__':
    # callbackにsay_helloのオブジェクトIDを格納する
    callback = say_hello
    handler(callback, 'user114514')
