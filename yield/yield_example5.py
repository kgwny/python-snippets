import os
import os.path

# 再帰呼び出し
def recursive_find_files(path):
    for x in os.listdir(path):
        join_path = os.path.join(path, x)
        if os.path.isdir(join_path):
            yield from recursive_find_files(join_path)
    else:
        yield join_path
