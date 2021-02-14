import subprocess
import sys

cp = subprocess.run(['ls', '-1'], encoding='utf-8', stdout=subprocess.PIPE)

print(f'*** file names: \n{cp.stdout}'
      f'*** total {len(cp.stdout.splitlines())} objects')
