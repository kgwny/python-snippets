list1 = ['item1', 'item2', 'item3']

print("list loop example part1")
index = 0
for item in list1:
    print("index:" + str(index) + ", value:" + item)
    index += 1

print("list loop example part2")
for index in range(len(list1)):
    print("index:" + str(index) + ", value:" + list1[index])

print("list loop example part3")
for index, item in enumerate(list1):
    print("index:" + str(index) + ", value:" + item)

print("double list loop example")
list2_1 = ['item1-1', 'item1-2', 'item1-3']
list2_2 = ['item2-1', 'item2-2', 'item2-3']
for index in range(len(list2_1)):
    print("list2_1:" + list2_1[index] + ", list2_2:" + list2_2[index])

print("double list loop with zip example part1")
list3_1 = ['item1-1', 'item1-2', 'item1-3']
list3_2 = ['item2-1', 'item2-2', 'item2-3']
for item3_1, item3_2 in zip(list3_1, list3_2):
    print("list3_1:" + item3_1 + ", list3_2:" + item3_2)

print("double list loop with zip example part2")
list4_1 = ['item1-1', 'item1-2', 'item1-3']
list4_2 = ['item2-1', 'item2-2', 'item2-3', 'item2-4']
for item4_1, item4_2 in zip(list4_1, list4_2):
    print("list4_1:" + item4_1 + ", list4_2:" + item4_2)

print("double list loop with zip example part3")
list5_1 = ['item1-1', 'item1-2', 'item1-3']
list5_2 = ['item2-1', 'item2-2', 'item2-3']
list5_3 = ['item3-1', 'item3-2', 'item3-3']
for item5_1, item5_2, item5_3 in zip(list5_1, list5_2, list5_3):
    print("list5_1:" + item5_1 + ", list5_2:" + item5_2 + ", list5_3:" + item5_3)

print("use append")
list6 = ['item1-1', 'item1-2', 'item1-3']
newList = []
for item in list6:
    newList.append(item + "-1")
print(newList)
# ['item1-1-1', 'item1-2-1', 'item1-3-1']

print("add string")
list7 = ['item1-1', 'item1-2', 'item1-3']
newList = [item + "-1" for item in list7]
print(newList) 
# ['item1-1-1', 'item1-2-1', 'item1-3-1']

print("filtering")
list8 = ['item1-1', 'item1-2', 'item1-3']
newList = [item + "-1" for item in list8 if not item.endswith("1")]
print(newList) 
# ['item1-2-1', 'item1-3-1']
