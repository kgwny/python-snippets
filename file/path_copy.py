import os
import shutil

# ./input配下にあるディレクトリ、ファイルを./output配下へコピーする

path_list = []

def recursive_path_check(path):
    # print(path)
    path_list.append(path)

    if os.path.isdir(path):
        dirs = os.listdir(path)
        for dir in dirs:
            recursive_path_check(path + '/' + dir)

input_path = './input'
output_path = './output'
recursive_path_check(input_path)
path_list.sort()
# print(path_list)

for path in path_list:
    new_path = path.replace('input', 'output')

    if os.path.isdir(path):
        if not os.path.isdir(new_path):
            os.mkdir(new_path)
    else:
        shutil.copyfile(path, new_path)
