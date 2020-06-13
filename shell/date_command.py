import subprocess
from subprocess import PIPE

# pythonでdateコマンドを実行する
proc = subprocess.run(['date'], shell=True, stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode('utf-8'))
print(proc.stderr.decode('utf-8'))
