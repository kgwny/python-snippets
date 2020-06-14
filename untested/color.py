
# 標準出力の文字を装飾する
class color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RETURN = '\033[07m'
    ACCENT = '\033[01m'
    FLASH = '\033[05m'
    RED_FLASH = '\033[05;41m'
    END = '\033[0m'

print(color.BLUE + '青色' + color.END)
print(color.ACCENT + '強調' + color.END)
print(color.RETURN + '反転' + color.END)
print(color.RED_FLASH + '赤 + 点滅' + color.END)
