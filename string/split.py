phrase = "How are you"
print(phrase.split())
# ["How", "are", "you"]

print(phrase.split(' '))
# ["How", "are", "you"]
# split()と挙動は同じ

word = "HelloWorld!"
print(word.rsplit("o", 1))
# ['HelloW', 'rld!']
