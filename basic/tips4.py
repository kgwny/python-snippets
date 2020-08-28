
# ディスクリプタ
# 親クラスに属している場合にのみ特殊な挙動をするクラス
class Person(object):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.parent = None

    def __get__(self, parent, klass):
        self.parent = parent
        return self

    @property
    def fullname(self):
        if self.parent:
            return self.parent.first_name + self.parent.last_name + self.first_name + self.last_name
        return self.first_name + self.last_name

# クラスのインスタンス生成
person = Person('山田', '太郎')
print(person.fullname)

# 親クラスからのインスタンス生成
class Company(Person):
    person = Person('山田', '太郎')

print(Company.person.fullname)

company = Company('株式会社', 'ほげほげ')

print(company.person.fullname)
