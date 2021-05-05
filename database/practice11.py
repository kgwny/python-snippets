# MySQLの接続例
# データベース、ユーザー、パスワード、ホスト、ポートを指定して接続できます。

from peewee import *
from datetime import date

db = MySQLDatabase(
    database='testdb',
    user='test',
    password="test",
    host="192.168.80.131",
    port=3306)

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the people database

db.create_tables([Person, Pet])

# 接続エラーが出る場合
# 下記のエラーが発生する場合はmysqlのドライバーをインストールしてください。
# peewee.ImproperlyConfigured: MySQL driver not installed!
# インストールの例：
# pip3 install mysqlclient
# peewee.ImproperlyConfigured: MySQL driver not installed!
