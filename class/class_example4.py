class Example:

    # __init__はコンストラクタ
    def __init__(self, a, b, c):
        self.num1 = a
        self.num2 = b
        self.num3 = c

    def print_sum(self):
        sum = self.num1 + self.num2 + self.num3
        print(sum)

myinstance = Example(1, 2, 3)
myinstance.print_sum()
