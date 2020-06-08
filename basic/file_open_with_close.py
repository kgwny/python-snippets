import os

test_file = "test.txt"

# make new file
if not os.path.exists(test_file):
    # w means write
    f = open(test_file, "w")
    f.write("Hello World!\n")
    f.close()
else:
    print("new file is alrady exist")
    # a means append
    f = open(test_file, "a")
    f.write("How are you doing?\n")
    f.close()

# read file
if os.path.exists(test_file):
    # r means read
    f = open(test_file, "r")
    print(f.read())
