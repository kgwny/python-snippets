# Cat class
class Cat(object):
    def __init__(self, name):
       self.name = name

# super class
class SuperCat(Cat):
    def __init__(self, name, function):
        super(SuperCat, self).__init__(name)
        self.function = function

cat1 = Cat('ミュウ')
print(cat1.name)

cat2 = SuperCat('ミュウ１', 'ダッシュ')
print(cat2.name, cat2.function)

cat3 = SuperCat('ミュウ２', 'ケリケリ')
print(cat3.name, cat3.function)
