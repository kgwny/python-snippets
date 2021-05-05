# 様々なデータベースへの接続方法
# peeweeでは様々なデータベースを使用できます。
# 詳細は下記を参照してください。
# https://peewee.readthedocs.org/en/latest/peewee/database.html

# SQLiteの接続例
# memoryまたはファイルを指定して接続ができます。

from peewee import *
from datetime import date

db = SqliteDatabase(':memory:')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db

db.create_tables([Person, Pet], True)
