# 変数
s = "str..."
l = ["1", "2", "3", "3", "4"]
t = ("A", "B", "C")
d = {"key": "value"}

s_ = str("str")
i_ = int("99")
f_ = float("100.0")
l_ = list((1,2,3))
d_ = dict([["key", "value"]])
e = set("0123456789")
ss = '''
dup
dup
dup
'''

# プリント構文
print(s, end="")

# スライス
s[0:1]
s[-1]
s[::1]

# 組み込み関数
len(s)
s.split()
",".join(l)
s.strip(".")
s.capitalize()
s.title()
s.upper()
s.lower()
s.swapcase()
s.replace(".", "!")
l.append("5")
l.insert(0, "10")
del l[0]
# l.remove("10")
l.pop()
l.index("1")
l.count("3")
l.sort()
c = l.copy()
d.keys()
d.values()
d.items()

# forループ
for val in l:
    print(val)

# 演算
False | True
True & True
1 > 0
0 >= 0

# if文
if s == "s":
    print("s!")
elif s == "str":
    print("str!")
else:
    print("!!!")

# whileループ
count = 0
while count < 3:
    print(count)
    count += 1

while True:
    print(count)
    if count == 5:
        break
    count += 1

# リスト内包表記
ll = [v for v in range(10)]

# 関数
def f(a,b):
    return a + b

# クラス
class S():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def rep(self):
        print(self.a + " " + self.b)

ss = S("Thank", "you")
ss.rep()
