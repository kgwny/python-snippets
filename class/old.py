# クラスの書式例
class Hoge:
    def __init__(self, hoge: str, fuga: int, piyo: bool):
        self.hoge = hoge
        self.fuga = fuga
        self.piyo = piyo

hoge = Hoge("hoge", 4649, False)
print(hoge)
