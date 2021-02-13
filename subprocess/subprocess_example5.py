import subprocess
from subprocess import PIPE

# 非同期
# サブプロセスを実行する
proc = subprocess.Popen('sleep 60; ls hoge.py aaa', shell=True, stdout=PIPE, stderr=PIPE, text=True)

# サブプロセスの完了を待つ
# ここではsleepしている60秒待たされる
result = proc.communicate()

(stdout, stderr) = (result[0], result[1])
print('STDOUT: {}'.format(stdout))
print('STDERR: {}'.format(stderr))
