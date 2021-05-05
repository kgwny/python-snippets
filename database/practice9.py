# 主キーの指定
# peeweeで主キーを指定する方法について以下で説明します。

# 主キーを設定しない場合
# PrimaryKeyを明示していない場合は、自動インクリメントのidという主キーを作成します。

class Test1(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

# 作成されるSQLiteのデータベース
# CREATE TABLE IF NOT EXISTS "test1" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL

# 特定のフィールドを主キーに指定する場合
# フィールドを作成する際にprimary_key=Trueと指定することで、該当のフィールドを主キーとします。

class Test2(Model):
    name = CharField(primary_key=True)
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

# 作成されるSQLiteのデータベース
# CREATE TABLE IF NOT EXISTS "test2" ("name" VARCHAR(255) NOT NULL PRIMARY KEY, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL)

# 複数のフィールドを主キーにする
# CompositeKeyを用いることで複数のフィールドを主キーにできます。

class Test3(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
        primary_key = CompositeKey('name', 'birthday')

# 作成されるSQLiteのデータベース
# CREATE TABLE IF NOT EXISTS "test3" ("name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL, PRIMARY KEY ("name", "birthday"))

# インデックスの指定
# peeweeでインデックスを指定する方法について以下で説明します。

# 指定の単一フィールドをインデックスにする
# フィールドを作成する際、index=Trueとすることでインデックスにできます

class Test4(Model):
    name = CharField(index=True)
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db

# 作成されるインデックス
# CREATE TABLE IF NOT EXISTS "test4" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL)
# CREATE INDEX IF NOT EXISTS "test4_name" ON "test4" ("name")

# 指定のフィールドを組み合わせてインデックスにする
# Meta クラスにてindexesを指定することで、複数のキーを組み合わせてインデックスを作成できます

class Test5(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
        indexes = (
            # 末尾に,がないとエラーになる
            # 複数指定も可能
            (('name', 'birthday'), False),
        )

# 作成されるインデックス
# CREATE TABLE IF NOT EXISTS "test5" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL)
# CREATE INDEX IF NOT EXISTS "test5_name_birthday" ON "test5" ("name", "birthday")

# 重複を禁止するインデックスにする
# フィールドを作成する際にunique=Trueを指定するか、Metaクラスのindexesの第二引数にTrueを指定することで重複を禁止するインデックスを作成できます。

class Test6(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db
        indexes = (
            # 末尾に,がないとエラーになる
            # 複数指定も可能
            (('name', 'birthday'), True),
        )

# 作成されるインデックス
# CREATE TABLE IF NOT EXISTS "test6" ("id" INTEGER NOT NULL PRIMARY KEY, "name" VARCHAR(255) NOT NULL, "birthday" DATE NOT NULL, "is_relative" INTEGER NOT NULL)
# CREATE UNIQUE INDEX IF NOT EXISTS "test6_name_birthday" ON "test6" ("name", "birthday")

# 外部キーについて
# ForeignKeyField()を使用すると外部キーが指定できます。
# to_field で主キー以外を指定できますが、このキーは主キーのいずれかであるか、一意制約を持つ必要があります。

# 301 Moved Permanentlyhttp://peewee.readthedocs.org
