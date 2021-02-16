from enum import IntEnum, auto

class Color(IntEnum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()

if __name__ == '__main__':
    print(int(Color.RED))  # 1
    print(int(Color.GREEN))  # 2
    print(int(Color.BLUE))  # 3
