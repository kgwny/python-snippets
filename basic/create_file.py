import os

target_file = "test.txt"

fruit = """apple
banana
cherry
"""

# create file
if not os.path.exists(target_file):
    # write
    with open(target_file, "w") as f:
        f.write(fruit)
else:
    # append
    with open(target_file, "a") as f:
        f.write(fruit)

# read
with open(target_file, "r") as f:
    print(f.read())

# remove file
os.remove(target_file)
