
# コンテキストマネージャー
# withステートメントによるファイルopen、ファイルcloseを行う仕組みに使われる
class ContextManager(object):
    def __enter__(self):
        print('enter')
        return 'ほげほげ'

    def __exit__(self, exc_type, exc_value, traceback):
        print('exit')

with ContextManager() as value:  # value == 'ほげほげ'
    # enterが呼び出される
    print(value)
    # exitが呼び出される
