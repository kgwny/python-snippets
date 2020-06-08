import os

target_file = "tmp.txt"

f = open(target_file, "w")
f.write("Hello World!\n")
f.close()

if os.path.exists(target_file):
    print("file created")

# remove file
os.remove(target_file)

if not os.path.exists(target_file):
    print("file deleted")
