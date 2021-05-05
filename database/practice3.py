from peewee import *
from datetime import date

# 大量データの作成
# 一度に大量のデータを作成する場合は、insert_manyを使用する

db = SqliteDatabase(':memory:')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

data_source = [
    {'name' : 'test1' , 'birthday' : date(1960, 1, 15), 'is_relative' : True},
    {'name' : 'test2' , 'birthday' : date(1960, 2, 15), 'is_relative' : True},
    {'name' : 'test3' , 'birthday' : date(1960, 3, 15), 'is_relative' : True},
    {'name' : 'test4' , 'birthday' : date(1960, 4, 15), 'is_relative' : True},
    {'name' : 'test5' , 'birthday' : date(1960, 5, 15), 'is_relative' : True},
]

db.create_tables([Person])
try:
    with db.transaction():
        Person.insert_many(data_source).execute()

    print ("全部取得-----------------")
    for person in Person.select():
        print (person.name, person.birthday, person.is_relative)

except IntegrityError as ex:
    print (ex)
    db.rollback()
