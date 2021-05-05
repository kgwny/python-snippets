# 条件を動的に組み立てる
# 下記の例では、operation_companyとrailway_lineを条件にクエリを取得しています。

def get_dynamic_sql(name = None, is_relative = None):
    ret = []
    query = Person.select()
    cond = None
    if not name is None:
        cond = (Person.name == name)
    if not is_relative is None:
        if cond:
            cond = cond & (Person.is_relative == is_relative)
        else:
            cond = (Person.is_relative == is_relative)
    rows = query.where(cond)
    for r in rows: # ここでSQLを発行する
        ret.append(r.name)
    return ret

# この例ではパラメータの指定方法により４種類のSQLが作成されます。

# name=None,is_relative=None
# SELECT "t1"."id", "t1"."name", "t1"."birthday", "t1"."is_relative" FROM "person" AS "t1

# name=None以外,is_relative=None
# SELECT "t1"."id", "t1"."name", "t1"."birthday", "t1"."is_relative" FROM "person" AS "t1" WHERE ("t1"."name" = ?)

# name=None,is_relative=None以外
# SELECT "t1"."id", "t1"."name", "t1"."birthday", "t1"."is_relative" FROM "person" AS "t1" WHERE ("t1"."is_relative" = ?)

# name=None以外,is_relative=None以外
# SELECT "t1"."id", "t1"."name", "t1"."birthday", "t1"."is_relative" FROM "person" AS "t1" WHERE (("t1"."name" = ?) AND ("t1"."is_relative" = ?))
