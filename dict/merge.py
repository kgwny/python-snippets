dict_1 = {'One': 1, 'Two': 2}
dict_2 = {'Two': 2, 'Three': 3}
dictionary_1 = {**dict_1, **dict_2}
print(dictionary_1)
# {'One': 1, 'Two': 2, 'Three': 3}

# Valueが異なる場合、どのようにマージされるのか？
dict_3 = {'Four': 4, 'Five': 4}
dict_4 = {'Five': 5, 'Six': 6}
dictionary_2 = {**dict_3, **dict_4}
print(dictionary_2)
# {'Four': 4, 'Five': 5, 'Six': 6}
# 結果として後勝ちになる

dictionary = {**dict_1, **dict_2, **dict_3, **dict_4}
print(dictionary)
# {'One': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6}
