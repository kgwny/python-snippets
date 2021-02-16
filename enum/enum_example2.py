from enum import IntEnum

class Color(IntEnum):
    RED = 1
    GREEN = 2
    BLUE = 3

def print_color(color):
    if color == Color.RED:
        print('Color is red')
    elif color == Color.GREEN:
        print('Color is green')
    elif color == Color.BLUE:
        print('Color is blue')
    else:
        print('not Color enum')

if __name__ == '__main__':
    print_color(Color.BLUE)  # Color is blue
    print_color(1)  # Color is red
    print(int(Color.RED))  # 1
