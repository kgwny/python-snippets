# callback function
def apply_async(func, args, callback):
    result = func(*args)
    callback(result)

def add(x, y):
    return x + y

def print_result(result):
    print('result:', result)

apply_async(add, (2, 3), callback=print_result)
# result: 5
apply_async(add, ('Hello', 'World'), callback=print_result)
# result: HelloWorld

# 以下と等価
print('result:', 2 + 3)
# result: 5
print('result:', 'HelloWorld')
# result: HelloWorld
