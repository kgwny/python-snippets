import os

test_file = "test.txt"

# make new file and write sentence
if not os.path.exists(test_file):
    # w means write
    f = open(test_file, "w")
    f.write("Hello World!\n")
    f.close()
else:
    print("new file is alrady exist")

# append new sentence
if os.path.exists(test_file):
    # a means append
    f = open(test_file, "a")
    f.write("How are you doing?\n")
    f.close()

# read file
if os.path.exists(test_file):
    # a means append
    f = open(test_file, "r")
    print(f.read())

fruit = """apple
banana
cherry
"""

# auto close, write file
with open(test_file, "w") as f:
    f.write(fruit)

# auto close, read file
with open(test_file, "r") as f:
    print(f.read())
