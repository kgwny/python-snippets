import subprocess
from subprocess import PIPE

print(os.getcwd())

# pythonでshellのコマンドを実行する
proc = subprocess.run("date", shell=True, stdout=PIPE, stderr=PIPE, text=True)
date = proc.stdout
print("stdout: {}".format(date))
