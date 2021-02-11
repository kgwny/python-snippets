import subprocess
from subprocess import PIPE

# 事前に下記コマンドを実行してfigletをいれておくこと
# brew install figlet

proc = subprocess.run(['figlet', 'Hello,'], stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode('utf-8'))
print(proc.stderr.decode('utf-8'))

proc = subprocess.run(['figlet', 'World!'], stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode('utf-8'))
print(proc.stderr.decode('utf-8'))
