
# bool 真偽値
true_val = bool(1)

print(type(true_val))
# <class 'bool'>
print(true_val)
# True

false_val = bool(0)

print(type(false_val))
# <class 'bool'>
print(false_val)
# False


if bool(1) == True:
    print("it is true")

if bool(1) != False:
    print("it is not false")
