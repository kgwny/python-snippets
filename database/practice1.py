from peewee import *
from datetime import date

db = SqliteDatabase(':memory:')

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


try:
    db.create_tables([Person, Pet])
    with db.transaction():
        # オブジェクトを作ってSaveすることでINSERTする
        uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
        uncle_bob.save() # bob is now stored in the database

        # createでINSERTする
        grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
        herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)

        bob_kitty = Pet.create(owner=uncle_bob, name='Kitty', animal_type='cat')
        herb_fido = Pet.create(owner=herb, name='Fido', animal_type='dog')
        herb_mittens = Pet.create(owner=herb, name='Mittens', animal_type='cat')
        herb_mittens_jr = Pet.create(owner=herb, name='Mittens Jr', animal_type='cat')

        print ("全部取得-----------------")
        for person in Person.select():
            print(person.name, person.is_relative)

        print("catのみ取得-----------------")
        query = Pet.select().where(Pet.animal_type == 'cat')
        for pet in query:
            print(pet.name, pet.owner.name)

        print("Joinの例-----------------")
        query = (Pet
                 .select(Pet, Person)
                 .join(Person)
                 .where(Pet.animal_type == 'cat'))
        for pet in query:
            print(pet.name, pet.owner.name)

        print("更新の例-----------------")
        update_pet = Pet.get(Pet.name=='Kitty')
        update_pet.name = 'Kitty(updated)'
        update_pet.save() 

        query = (Pet
                 .select(Pet, Person)
                 .join(Person)
                 .where(Pet.animal_type == 'cat'))
        for pet in query:
            print(pet.name, pet.owner.name)


        print("削除の例-----------------")
        del_pet = Pet.get(Pet.name=='Mittens Jr')
        del_pet.delete_instance() 

        query = (Pet
                 .select(Pet, Person)
                 .join(Person)
                 .where(Pet.animal_type == 'cat'))
        for pet in query:
            print(pet.name, pet.owner.name)

        db.commit()


except IntegrityError as ex:
    print (ex)
    db.rollback()
