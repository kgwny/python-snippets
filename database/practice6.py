# JOINについて
# 使用できるJOIN
# peewee 2.4.5ではRIGHTやFULL JOINはできません。
# INNER JOIN か LEFT OUTER JOINのみ使用できます。
# query = Curve.select(Curve, RailRoadSection).join(RailRoadSection, JOIN_FULL)
# JOIN_FULLを指定した場合、例外が発生します。
# peewee.OperationalError: RIGHT and FULL OUTER JOINs are not currently supported

# LEFT OUTER JOINの例
# 取得したレコードに結合中のテーブル名があります。dir関数でレコードの内容をするといいでしょう。

# モデル
from peewee import *
from datetime import date

db = SqliteDatabase(':memory:')

class Group(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()
    group = ForeignKeyField(Group, related_name='group')

    class Meta:
        database = db # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets', null=True)
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the people database




try:
    db.create_tables([Person, Pet, Group])
    with db.transaction():
        # 
        grp1 = Group(name='花組')
        grp1.save()
        grp2 = Group(name='奇面組')
        grp2.save()

        # オブジェクトを作ってSaveすることでINSERTする
        uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True, group=grp1)
        uncle_bob.save() # bob is now stored in the database

        # createでINSERTする
        grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True, group=grp2)
        herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False, group=grp1)

        bob_kitty = Pet.create(owner=herb, name='Kitty', animal_type='cat')
        herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
        herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
        herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')
        ginga = Pet.create(owner=None, name='Mittens Jr', animal_type='cat')


        print ("全部取得-----------------")
        for group in Group.select():
            print(group.name)
        for person in Person.select():
            print(person.name, person.is_relative, person.group)
        for pet in Pet.select():
            print(pet.owner, pet.name, pet.animal_type)


        print("inner Joinの例-----------------")
        query = (Pet
                 .select(Pet, Person)
                 .join(Person))
        for pet in query:
            print(pet.name, pet.owner.name)


        print("left outer Joinの例-----------------")
        query = (Pet
                 .select(Pet, Person)
                 .join(Person, JOIN.LEFT_OUTER))
        for pet in query:
            print(pet.name, pet.owner)

        #print("right outer Joinの例-----------------")
        #query = (Pet
        #         .select(Pet, Person)
        #         .join(Person, JOIN.FULL))
        #for pet in query:
        #    print(pet.name, pet.owner)

except IntegrityError as ex:
    print (ex)
    db.rollback()
