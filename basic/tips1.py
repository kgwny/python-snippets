
# アンスコをカンマへ置換する
ten_billion = 10_000_000_000

print(f'{ten_billion:,}')
# 10,000,000,000

# ------------------------------

# general
isHappy = True

if isHappy == True:
    result_string = 'Happy'
else:
    result_string = 'Not Happy'

print(result_string)
# Happy

# 三項演算子
isHappy = True

result_string = 'Happy' if isHappy else 'Not Happy'

print(result_string)
# Happy

# ------------------------------

# general
low = 10
high = 9

if low > high:
    temp = low
    low = high
    high = temp

print(low, high)
# 9 10

# advanced
low = 10
high = 9

if low > high:
    low, high = high, low

print(low, high)
# 9 10

# ------------------------------

# general
grades = ['A', 'B', 'C', 'D', 'E', 'F']

i = 1
for grade in grades:
    print(f'{i} : {grade}')
    i += 1

# 1 : A
# 2 : B
# 3 : C
# 4 : D
# 5 : E
# 6 : F

# advanced
grades = ['A', 'B', 'C', 'D', 'E', 'F']

for i, grade in enumerate(grades, 1):
    print(f'{i} : {grade}')

# 1 : A
# 2 : B
# 3 : C
# 4 : D
# 5 : E
# 6 : F

# ------------------------------

# beginner
numbers = [1, 2, 3, 4, 5, 6, 7]

squared = []
for number in numbers:
    squared.append(number * number)

print(squared)
# [1, 4, 9, 16, 25, 36, 49]

# advanced
numbers = [1, 2, 3, 4, 5, 6, 7]

squared = [number * number for number in numbers]

print(squared)
# [1, 4, 9, 16, 25, 36, 49]

# ------------------------------

# from 13 cards
cards = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K' )

# extract ace, 2, 3 only
ace, two, three, *_ = cards
print(ace, two, three)
# A 2 3


# extract ace, [numbers], J, Q, K
ace, *numbers, J, Q, K = cards
print(ace, numbers, J, Q, K)
# A ['2', '3', '4', '5', '6', '7', '8', '9', '10'] J Q K

# ------------------------------

# For ~ Else
grades = ['A', 'B', 'C', 'D', 'E', 'F']

my_grade = 'A+'

for grade in grades:
    if grade == my_grade:
        print('grade found')
        break
else:
    print('grade not found')
# grade not found

# ------------------------------
