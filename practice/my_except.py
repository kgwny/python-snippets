class MyError(Exception):
    def __init__(self, file, line):
        self.file = file
        self.line = line

try:
    raise MyError('temp.txt', 120)
except MyError as e:
    print('MyError')
    print(e.file)
    print(e.line)
