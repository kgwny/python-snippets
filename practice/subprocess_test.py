import subprocess

# terminalのコマンドを実行する

# 標準出力にコマンドの実行結果が表示される
# subprocess.call(['ls', '-l'])

# 標準出力にコマンドの実行結果が表示される
# ただし、処理に失敗した場合はpythonの異常系のエラーメッセージを出力する
# subprocess.check_call(['ls', '-l'])

# コマンドの実行結果を変数に代入することができる
# 変数に代入される値はバイト文字列なので注意すること
# ただし、処理に失敗した場合はpythonの異常系のエラーメッセージを出力する
result = subprocess.check_output(['ls', '-l'])
print(result.decode())
