import os

wk_dir = os.getcwd()
print('current dir:', wk_dir)

# change dir
os.chdir('../')

wk_dir = os.getcwd()
print('changed dir:', wk_dir)
