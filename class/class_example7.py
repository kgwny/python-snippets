class Hoge:

    def __init__(self):
        self.__attr = '値'

    # 文字列化
    def __str__(self):
        return 'value = ' + self.__attr 

hoge = Hoge()
print(hoge)
