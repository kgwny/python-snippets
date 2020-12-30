import os

path_list = []

def recursive_path_check(path):
    print(path)
    path_list.append(path)
    if os.path.isdir(path):
        dirs = os.listdir(path)
        for dir in dirs:
            recursive_path_check(path + '/' + dir)

root_path = '.'
recursive_path_check(root_path)
# print(path_list)
