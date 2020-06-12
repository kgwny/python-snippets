import subprocess
from subprocess import PIPE

array = [i for i in range(100)]
input_text = "\n".join(array)
proc = subprocess.run("cat -n", shell=True, input=input_text, stdout=PIPE, stderr=PIPE, text=True)
print(proc.stdout)
