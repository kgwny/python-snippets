# 動物クラス
class Animal:
    def __init__(self, name, build="タンパク質", eyelids=False):
        self.name = name
        self.build = build 
        self.eyelids = eyelids

    # 独自メソッド1
    def walk(self):
        print("この動物は歩行する")

    # 独自メソッド2
    def run(self):
        print("この動物は走る")

# クラスの継承(inheritance)
# 書式：class 新規クラス名（継承したいクラス名）:
class Human(Animal):
    print("開始")
    pass
    print("終了")
