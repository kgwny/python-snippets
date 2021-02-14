import subprocess
from subprocess import PIPE

# 非同期
# サブプロセスを実行する
proc = subprocess.Popen('sleep 10; ls hoge.py aaa', shell=True, stdout=PIPE, stderr=PIPE, text=True)

# サブプロセスの完了を待つ
# ここではsleepしている60秒待たされる
result = proc.communicate()

(stdout, stderr) = (result[0], result[1])
print('STDOUT: {}'.format(stdout))
print('STDERR: {}'.format(stderr))

# subprocess.runは同期処理
# サブプロセスが終了するまでは次の処理に進まない

# subprocess.Popenは非同期処理
# subprocess.Popenでサブプロセスの処理を開始して
# communicateでサブプロセスの終了を待ち
# 終了すると出力結果を取得する

# subprocess.Popenとsubprocess.runの相違点
# subprocess.Popenはinputを指定することができない

# communicateにはinputを渡すことができるものの、同期処理になってしまうのが問題点
# Pythonの変数に格納されている値を非同期処理の入力に橋渡しする検討が必要
