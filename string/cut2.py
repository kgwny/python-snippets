
file_path = '/User/admin/Documents/text_file.txt'

tmp1 = file_path.replace('.txt', '')
print(tmp1)

tmp2 = file_path.split('.')[0]
print(tmp2)

print(tmp1 == tmp2)
