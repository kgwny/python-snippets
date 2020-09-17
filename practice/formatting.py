
print("My name is {} and I'm {} years old.".format('kgwny','20'))

d = {'name': 'kgwny', 'age': 20}
print("My name is %(name)s and I'm %(age)i years old." % d)

d = {'name': 'kgwny', 'age': 20}
print("My name is {name} and I'm {age} years old.".format(**d))

c = {'email': 'hoge@example.com', 'phone': '0000-0000'}
print('My name is {0[name]}, my email is {1[email]} and my phone number is {1[phone]}'.format(d, c))

class Person:
    pass

me = Person()
me.name = 'kgwny'
me.email = 'hoge@example.com'
me.phone = '0000-0000'
print('My name is {me.name}, my email is {me.email} and my phone number is {me.phone}'.format(me=me))
