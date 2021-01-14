line = 'hoge\n'
msg = line.rstrip() + 'moge'
print(msg)

with open('./tmp/test.txt') as fh:
    for line in fh:
        no_line_break_line = line.rstrip()
        print(no_line_break_line)

line_with_space = 'line \n'
print(line_with_space.rstrip('\n'))
