from enum import Enum

class Color(Enum):
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
    print_color(Color.BLUE)
    # Color is blue

    print_color(1)
    # not Color enum

    print(Color)
    # <enum 'Color'>

    print(Color(1))
    # Color.RED

    print(Color.RED == Color.RED)
    # True

    print(Color.RED == Color.GREEN)
    # False

    for color in Color:
        print(color)
        # Color.RED\nColor.GREEN\nColor.BLUE
