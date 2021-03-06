# python でメソッドの一覧を取得する方法
import inspect

obj = "abc"

for m in inspect.getmembers(obj):
    print(m)

# ('__add__', <method-wrapper '__add__' of str object at 0x10e569cb0>)
# ('__class__', <class 'str'>)
# ('__contains__', <method-wrapper '__contains__' of str object at 0x10e569cb0>)
# ('__delattr__', <method-wrapper '__delattr__' of str object at 0x10e569cb0>)
# ('__dir__', <built-in method __dir__ of str object at 0x10e569cb0>)
# ('__doc__', "str(object='') -> str\nstr(bytes_or_buffer[, encoding[, errors]]) -> str\n\nCreate a new string object from the given object. If encoding or\nerrors is specified, then the object must expose a data buffer\nthat will be decoded using the given encoding and error handler.\nOtherwise, returns the result of object.__str__() (if defined)\nor repr(object).\nencoding defaults to sys.getdefaultencoding().\nerrors defaults to 'strict'.")
# ('__eq__', <method-wrapper '__eq__' of str object at 0x10e569cb0>)
# ('__format__', <built-in method __format__ of str object at 0x10e569cb0>)
# ('__ge__', <method-wrapper '__ge__' of str object at 0x10e569cb0>)
# ('__getattribute__', <method-wrapper '__getattribute__' of str object at 0x10e569cb0>)
# ('__getitem__', <method-wrapper '__getitem__' of str object at 0x10e569cb0>)
# ('__getnewargs__', <built-in method __getnewargs__ of str object at 0x10e569cb0>)
# ('__gt__', <method-wrapper '__gt__' of str object at 0x10e569cb0>)
# ('__hash__', <method-wrapper '__hash__' of str object at 0x10e569cb0>)
# ('__init__', <method-wrapper '__init__' of str object at 0x10e569cb0>)
# ('__init_subclass__', <built-in method __init_subclass__ of type object at 0x10e34d3b0>)
# ('__iter__', <method-wrapper '__iter__' of str object at 0x10e569cb0>)
# ('__le__', <method-wrapper '__le__' of str object at 0x10e569cb0>)
# ('__len__', <method-wrapper '__len__' of str object at 0x10e569cb0>)
# ('__lt__', <method-wrapper '__lt__' of str object at 0x10e569cb0>)
# ('__mod__', <method-wrapper '__mod__' of str object at 0x10e569cb0>)
# ('__mul__', <method-wrapper '__mul__' of str object at 0x10e569cb0>)
# ('__ne__', <method-wrapper '__ne__' of str object at 0x10e569cb0>)
# ('__new__', <built-in method __new__ of type object at 0x10e34d3b0>)
# ('__reduce__', <built-in method __reduce__ of str object at 0x10e569cb0>)
# ('__reduce_ex__', <built-in method __reduce_ex__ of str object at 0x10e569cb0>)
# ('__repr__', <method-wrapper '__repr__' of str object at 0x10e569cb0>)
# ('__rmod__', <method-wrapper '__rmod__' of str object at 0x10e569cb0>)
# ('__rmul__', <method-wrapper '__rmul__' of str object at 0x10e569cb0>)
# ('__setattr__', <method-wrapper '__setattr__' of str object at 0x10e569cb0>)
# ('__sizeof__', <built-in method __sizeof__ of str object at 0x10e569cb0>)
# ('__str__', <method-wrapper '__str__' of str object at 0x10e569cb0>)
# ('__subclasshook__', <built-in method __subclasshook__ of type object at 0x10e34d3b0>)
# ('capitalize', <built-in method capitalize of str object at 0x10e569cb0>)
# ('casefold', <built-in method casefold of str object at 0x10e569cb0>)
# ('center', <built-in method center of str object at 0x10e569cb0>)
# ('count', <built-in method count of str object at 0x10e569cb0>)
# ('encode', <built-in method encode of str object at 0x10e569cb0>)
# ('endswith', <built-in method endswith of str object at 0x10e569cb0>)
# ('expandtabs', <built-in method expandtabs of str object at 0x10e569cb0>)
# ('find', <built-in method find of str object at 0x10e569cb0>)
# ('format', <built-in method format of str object at 0x10e569cb0>)
# ('format_map', <built-in method format_map of str object at 0x10e569cb0>)
# ('index', <built-in method index of str object at 0x10e569cb0>)
# ('isalnum', <built-in method isalnum of str object at 0x10e569cb0>)
# ('isalpha', <built-in method isalpha of str object at 0x10e569cb0>)
# ('isascii', <built-in method isascii of str object at 0x10e569cb0>)
# ('isdecimal', <built-in method isdecimal of str object at 0x10e569cb0>)
# ('isdigit', <built-in method isdigit of str object at 0x10e569cb0>)
# ('isidentifier', <built-in method isidentifier of str object at 0x10e569cb0>)
# ('islower', <built-in method islower of str object at 0x10e569cb0>)
# ('isnumeric', <built-in method isnumeric of str object at 0x10e569cb0>)
# ('isprintable', <built-in method isprintable of str object at 0x10e569cb0>)
# ('isspace', <built-in method isspace of str object at 0x10e569cb0>)
# ('istitle', <built-in method istitle of str object at 0x10e569cb0>)
# ('isupper', <built-in method isupper of str object at 0x10e569cb0>)
# ('join', <built-in method join of str object at 0x10e569cb0>)
# ('ljust', <built-in method ljust of str object at 0x10e569cb0>)
# ('lower', <built-in method lower of str object at 0x10e569cb0>)
# ('lstrip', <built-in method lstrip of str object at 0x10e569cb0>)
# ('maketrans', <built-in method maketrans of type object at 0x10e34d3b0>)
# ('partition', <built-in method partition of str object at 0x10e569cb0>)
# ('replace', <built-in method replace of str object at 0x10e569cb0>)
# ('rfind', <built-in method rfind of str object at 0x10e569cb0>)
# ('rindex', <built-in method rindex of str object at 0x10e569cb0>)
# ('rjust', <built-in method rjust of str object at 0x10e569cb0>)
# ('rpartition', <built-in method rpartition of str object at 0x10e569cb0>)
# ('rsplit', <built-in method rsplit of str object at 0x10e569cb0>)
# ('rstrip', <built-in method rstrip of str object at 0x10e569cb0>)
# ('split', <built-in method split of str object at 0x10e569cb0>)
# ('splitlines', <built-in method splitlines of str object at 0x10e569cb0>)
# ('startswith', <built-in method startswith of str object at 0x10e569cb0>)
# ('strip', <built-in method strip of str object at 0x10e569cb0>)
# ('swapcase', <built-in method swapcase of str object at 0x10e569cb0>)
# ('title', <built-in method title of str object at 0x10e569cb0>)
# ('translate', <built-in method translate of str object at 0x10e569cb0>)
# ('upper', <built-in method upper of str object at 0x10e569cb0>)
# ('zfill', <built-in method zfill of str object at 0x10e569cb0>)