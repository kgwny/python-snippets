class MyClass:
    """A simple example class"""         # 三重クォートによるコメント

    def __init__(self):                  # コンストラクタ
        self.name = ""

    def getName(self):                   # ゲッター
        return self.name

    def setName(self, name):             # セッター
        self.name = name

def print_method_list(obj):
    for x in dir(obj):
        print(x, ':', type(eval("obj." + x)))

a = MyClass()                            # クラスのインスタンスを生成
a.setName("taro yamada")                 # setName()メソッドをコール
print(a.getName())                       # getName()メソッドをコール
print_method_list(a)
# __class__ : <class 'type'>
# __delattr__ : <class 'method-wrapper'>
# __dict__ : <class 'dict'>
# __dir__ : <class 'builtin_function_or_method'>
# __doc__ : <class 'str'>
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
# getName : <class 'method'>
# name : <class 'str'>
# setName : <class 'method'>
