in_file_path = './tmp.txt'

# ファイルの行を返すジェネレータ
def file_line_reader_generator(file_path):
    with open(file_path, encoding='utf-8') as in_file:
        for line in in_file:
            yield line

file_lines = file_line_reader_generator(in_file_path)

print(file_lines)
# <generator object file_line_reader_generator at 0x100f281a8>

for line in file_lines:
    print(line)
