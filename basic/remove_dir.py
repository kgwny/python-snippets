import os

target_dir = "tmp"

# create dir
os.makedirs(target_dir, exist_ok=True)

if os.path.exists(target_dir):
    print("dir created")

# remove dir
os.rmdir(target_dir)

if not os.path.exists(target_dir):
    print("dir deleted")
