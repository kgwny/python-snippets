# オブジェクトのメソッド名をすべて取得する方法
def print_method_list(obj):
    for x in dir(obj):
        print(x, ':', type(eval("obj." + x)))

# print(type(obj))
# for x in inspect.getmembers(obj, inspect.ismethod):
#     print(x[0])

# サンプルのクラス
class Country:
    def __init__(self, country_name):
        self.country_name = country_name

c = Country('Japan')
print_method_list(c)
# __class__ : <class 'type'>
# __delattr__ : <class 'method-wrapper'>
# __dict__ : <class 'dict'>
# __dir__ : <class 'builtin_function_or_method'>
# __doc__ : <class 'NoneType'>
# __eq__ : <class 'method-wrapper'>
# __format__ : <class 'builtin_function_or_method'>
# __ge__ : <class 'method-wrapper'>
# __getattribute__ : <class 'method-wrapper'>
# __gt__ : <class 'method-wrapper'>
# __hash__ : <class 'method-wrapper'>
# __init__ : <class 'method'>
# __init_subclass__ : <class 'builtin_function_or_method'>
# __le__ : <class 'method-wrapper'>
# __lt__ : <class 'method-wrapper'>
# __module__ : <class 'str'>
# __ne__ : <class 'method-wrapper'>
# __new__ : <class 'builtin_function_or_method'>
# __reduce__ : <class 'builtin_function_or_method'>
# __reduce_ex__ : <class 'builtin_function_or_method'>
# __repr__ : <class 'method-wrapper'>
# __setattr__ : <class 'method-wrapper'>
# __sizeof__ : <class 'builtin_function_or_method'>
# __str__ : <class 'method-wrapper'>
# __subclasshook__ : <class 'builtin_function_or_method'>
# __weakref__ : <class 'NoneType'>
# country_name : <class 'str'>
