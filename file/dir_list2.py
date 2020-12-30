import os

def recursive_path_check(path):
    # パスがディレクトリの場合、ディレクトリに対して再帰的に実行する
    if os.path.isdir(path):
        print(path)
        dirs = os.listdir(path)
        for dir in dirs:
            recursive_path_check(path + '/' + dir)

root_path = '.'
recursive_path_check(root_path)
