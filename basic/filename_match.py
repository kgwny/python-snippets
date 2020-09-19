
# ファイル名の確認
filename = 'test.txt'

if filename in ['text.txt', 'text.md']:
    print('text', 'true')

if filename in ['test.txt', 'test.md']:
    print('test', 'true')

if filename in ['hoge.txt', 'hoge.md']:
    print('hoge', 'true')
