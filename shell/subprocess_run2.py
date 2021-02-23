import subprocess
from subprocess import PIPE

# 自作のシェルスクリプトを呼び出す

AA_SH = 'aa.sh'
proc = subprocess.run(['sh', AA_SH], stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode('utf-8'))
print(proc.stderr.decode('utf-8'))
