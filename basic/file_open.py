import os

test_file = "test.txt"

fruit = """apple
banana
cherry
"""

# make new file
if not os.path.exists(test_file):
    # write file
    with open(test_file, "w") as f:
        f.write(fruit)
else:
    # write file (append)
    with open(test_file, "a") as f:
        f.write(fruit)

# read file
with open(test_file, "r") as f:
    print(f.read())
