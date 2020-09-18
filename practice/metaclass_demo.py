
class MetaClass(type):
    def __new__(klass, name, bases, attrs):
        new_class = super(MetaClass, klass).__new__(klass, name, bases, attrs)

        silent = attrs.get('hoge', False)

        if silent:
            new_class.say = lambda s: print('fugafuga')

        return new_class

class Person(object):
    def say(self):
        print('hogehoge')

class Yama(Person, metaclass=MetaClass):
    hoge = False

class Kawa(Person, metaclass=MetaClass):
    hoge = True

Yama().say()
# hogehoge

Kawa().say()
# fugafuga
