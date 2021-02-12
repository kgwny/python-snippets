import subprocess
from subprocess import PIPE

# 自作のシェルスクリプトを呼び出す

proc = subprocess.run(['sh', 'aa.sh'], stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode('utf-8'))
print(proc.stderr.decode('utf-8'))
