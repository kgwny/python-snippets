import os

# make new dir
new_dir_path = "new"

if not os.path.exists(new_dir_path):
    os.makedirs(new_dir_path)
    print("make new dir: done")
else:
    print("new dir is already exist")

print(os.getcwd() + "/" + new_dir_path)
