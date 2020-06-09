import os

target_dir = "tmp"

if not os.path.exists(target_dir):
    # create dir
    os.makedirs(target_dir, exist_ok=True)
    print("create dir")
else:
    print("target dir is already exist")

print(os.getcwd() + "/" + target_dir)

# remove dir
os.rmdir(target_dir)
