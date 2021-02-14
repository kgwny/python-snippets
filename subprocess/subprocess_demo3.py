import subprocess
import sys

with open('out.txt', 'w') as fp:
    cp = subprocess.run(['ls', '-1'], encoding='utf-8', stdout=fp)
