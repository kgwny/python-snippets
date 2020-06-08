import os

target_file = "test.txt"

# create file
if not os.path.exists(target_file):
    # write
    f = open(target_file, "w")
    f.write("Hello World!\n")
    f.close()
else:
    print("new file is alrady exist")
    # append
    f = open(target_file, "a")
    f.write("How are you doing?\n")
    f.close()

# read
f = open(target_file, "r")
print(f.read())

# remove file
os.remove(target_file)
