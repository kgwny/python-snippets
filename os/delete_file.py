import os
import glob

wk_dir = os.getcwd()
print('work_dir:', wk_dir)

target_file = 'tmp.txt'

if not os.path.exists(target_file):
    f = open(target_file, 'w')
    f.write('')
    f.close()
    print('target_file is created.')

# delete file: target_file
os.remove(target_file)

if not os.path.exists(target_file):
    print('target_file is deleted.')
