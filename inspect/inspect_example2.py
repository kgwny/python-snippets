import hoge
import inspect

print(inspect.getmembers(hoge, inspect.isclass))
# [('fugu', <class 'hoge.fugu'>), ('ika', <class 'hoge.ika'>), ('tako', <class 'hoge.tako'>)]
