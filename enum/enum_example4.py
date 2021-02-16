from enum import Flag, auto

class Color(Flag):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    PURPLE = RED | BLUE
    WHITE = RED | GREEN | BLUE

def print_color(color):
    if color == Color.RED:
        print('Color is red')
    elif color == Color.GREEN:
        print('Color is green')
    elif color == Color.BLUE:
        print('Color is blue')
    elif color == Color.PURPLE:
        print('Color is purple')
    elif color == Color.WHITE:
        print('Color is white')
    else:
        print('not defined')

if __name__ == '__main__':
    print_color(Color.BLUE)
    # Color is blue

    print_color(Color.PURPLE)
    # Color is purple

    print_color(Color.RED | Color.BLUE)
    # Color is purple

    print_color(Color.RED | Color.GREEN)
    # not defined

    print_color(Color.WHITE)
    # Color is white

    print_color(Color.RED | Color.GREEN | Color.BLUE)
    # Color is white
