import functools

def makebold(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<b>" + func(*args, **kwargs) + "</b>"
    return wrapper

def makeitalic(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return "<i>" + func(*args, **kwargs) + "</i>"
    return wrapper

@makebold
@makeitalic
def hello(your_name):
    return "hello {0}.".format(your_name)

print(hello("hoge"))
# <b><i>hello hoge.</i></b>
