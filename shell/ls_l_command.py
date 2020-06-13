import subprocess
from subprocess import PIPE

proc = subprocess.run(['ls', '-l'], encoding='utf-8', stdout=subprocess.PIPE)

print(type(proc))

print(f'file names: \n{proc.stdout}'
      f'total {len(proc.stdout.splitlines())} files')
