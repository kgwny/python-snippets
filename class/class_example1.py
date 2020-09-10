# 国クラス
class Country:
    def __init__(self, country_name):
        self.country_name = country_name

# 都市クラス
class City(Country):
    def __init__(self, country_name, city_name):
        super().__init__(country_name)
        self.city_name = city_name

# 国クラスの使用
c = Country('England')
print('country_name = ' + c.country_name)

# 都市クラスの使用
classes = []
classes.append(City('Japan', 'Tokyo'))
classes.append(City('USA', 'Washington, D.C.'))

for test_cls in classes:
    print('country_name = ' + test_cls.country_name)
    # country_name --> Japan
    # city_name --> Tokyo
    print('city_name = ' + test_cls.city_name)
    # country_name --> USA
    # city_name --> Washington, D.C.
