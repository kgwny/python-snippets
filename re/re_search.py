import re

s = '012-3456-7890'
print(re.search(r'\d+', s))
# <re.Match object; span=(0, 3), match='012'>

m = re.search(r'\d+', s)
print(m.group())
# 012
print(type(m.group()))
# <class 'str'>

print(re.findall(r'\d+', s))
# ['012', '3456', '7890']

yyyymm = re.findall(r'\d{4}-\d{2}', '2020-01-31')
print(len(yyyymm))
print(yyyymm[0])
# 2020-01

yyyymm = re.findall(r'^\d{4}-\d{2}', '20200-999-31')
print(len(yyyymm))
print(yyyymm)
