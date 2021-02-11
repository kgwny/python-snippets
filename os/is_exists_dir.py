import os

wk_dir = os.getcwd()
print('work_dir:', wk_dir)

target_dir = 'hogehoge'

if os.path.exists(target_dir):
    print('target_dir exists.')
else:
    print('target_dir not exists.')
