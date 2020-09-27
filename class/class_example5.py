class Hoge:

    # コンストラクタ
    def __init__(self, ika, tako):
        self.ika = ika
        self.tako = tako

    def output(self):
        sum = self.ika + self.tako
        print("{0}".format(sum))

hoge = Hoge(5, 10)
hoge.output()
