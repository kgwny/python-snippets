import subprocess
from subprocess import PIPE

# 0-100
num_list = [str(i) for i in range(100)]
input_text = '\n'.join(num_list)

# 変数をstdinとしてサブプロセスに渡す
proc = subprocess.run('cat -n', shell=True, input=input_text, stdout=PIPE, stderr=PIPE, text=True)
print(proc.stdout)
