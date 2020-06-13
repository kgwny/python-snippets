import os
import pathlib

target_file = 'blank.txt'

# create file
target_path = pathlib.Path(target_file)
target_path.touch()

if os.path.exists(target_file):
    print(target_file + ' is created')

# remove file
os.remove(target_file)
