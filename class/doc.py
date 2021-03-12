class MyClass:
    'This is an example.'
    pass

# ドキュメンテーション文字列
print(MyClass.__doc__)
# This is an example.

# helpの表示

# 間違った使い方
help(MyClass.__doc__)
# No Python documentation found for 'This is an example.'.
# Use help() to get the interactive help utility.
# Use help(str) for help on the str class.

help(MyClass)
# Help on class MyClass in module __main__:
# 
# class MyClass(builtins.object)
#  |  This is an example.
#  |  
#  |  Data descriptors defined here:
#  |  
#  |  __dict__
#  |      dictionary for instance variables (if defined)
#  |  
#  |  __weakref__
#  |      list of weak references to the object (if defined)
