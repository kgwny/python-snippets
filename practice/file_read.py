
input_path = "./data.txt"

with open(input_path, 'r') as f:
    content = f.read()

content = content.format('hogehoge')
print(content)
