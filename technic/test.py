class Person():
    pass

person = Person()

person_info = {'first':'Taro', 'last':'Yamada'}

# setattr
for key, value in person_info.items():
    setattr(person, key, value)

# getattr
for key in person_info.keys():
    print(getattr(person, key))
