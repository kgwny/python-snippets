# DISTINCTの使用方法
# DISTINCTは下記のように利用します。

    q = Person.select(Person.name).distinct()
    print (q.sql())
    for person in q:
        print (person.name, person.birthday, person.is_relative)

# 作成されるSQLは下記のようになります。
'('SELECT DISTINCT "t1"."name" FROM "person" AS "t1"', [])
