import os
import glob

wk_dir = os.getcwd()
print('work_dir:', wk_dir)

target_dir = 'tmp'

if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('target_dir is created.')

# delete dir: target_dir
os.rmdir(target_dir)
# os.remove(target_dir)では削除できないので注意

if not os.path.exists(target_dir):
    print('target_dir is deleted.')
