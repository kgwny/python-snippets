import subprocess
from subprocess import PIPE

with open("input.txt") as input_file:
    with open("output.txt", "w") as output_file:
        proc = subprocess.run("cat -n", shell=True, stdin=input_file, stdout=output_file, text=True)
