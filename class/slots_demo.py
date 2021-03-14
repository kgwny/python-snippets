class Point1(object):
    def __init__(self):
        self.x = 0
        self.y = 0

# クラスのサイズを取得
import sys
print(sys.getsizeof(Point1))
# 1064

class Point2(object):
    # __slots__を定義
    __slots__ = ['x', 'y']

    def __init__(self):
        self.x = 0
        self.y = 0

# クラスのサイズを取得
print(sys.getsizeof(Point2))
# 896

# __slots__ を使うときは、以下の条件を満たす必要がある
# attributeの追加がないクラス
# 多数のインスタンスが予想されるクラス or 動作速度が非常に重要なクラス
