def handler(func, *args):
    return func(*args)

def function1(hoge):
    return hoge

def function2(hoge, huga):
    return hoge, huga

# 関数辞書
func_dict = {'func1': function1, 'func2': function2}

hoge = 'hoge'
huga = 'huga'

result1 = handler(func_dict['func1'], hoge)
result2, result3 = handler(func_dict['func2'], hoge, huga)

print('result1 =', result1)
print('result2 =', result2)
print('result3 =', result3)
