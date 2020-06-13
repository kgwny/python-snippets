import os
import subprocess
from subprocess import PIPE

# create file
f = open('input.txt', 'w')
f.write('line1\n')
f.write('line2\n')
f.write('line3\n')
f.close()

with open('input.txt') as input_file:
    with open('output.txt', 'w') as output_file:
        proc = subprocess.run(['cat -n'], shell=True, stdin=input_file, stdout=output_file)

# read file
f = open('output.txt', 'r')
print(f.read())

# remove file
os.remove('input.txt')
os.remove('output.txt')
