from getpass import getpass

username = input('name: ')

# パスワード入力のときにコマンドラインに表示しない
password = getpass('pass: ')
repassword = getpass('pass again: ')

print('Logging in...')
