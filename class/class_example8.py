class Hoge:
    id :int = 0
    name :str = None

    def __init__(self, id :int, name :str):
        self.id = id
        self.name = name

    def __str__(self):
        return 'id = ' + str(self.id) + ', name = ' + self.name

    def __repr__(self):
        return self.__str__()

# objectをeval()で再び元のオブジェクトに戻せる文字列に変換して返す
# representationの略

hoge = Hoge(1, 'hoge')
print(hoge)
