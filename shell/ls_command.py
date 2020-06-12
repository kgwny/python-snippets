import subprocess
from subprocess import PIPE

proc = subprocess.run(["ls"], stdout=PIPE, stderr=PIPE)
print(proc.stdout.decode("utf-8"))
print(proc.stderr.decode("utf-8"))
