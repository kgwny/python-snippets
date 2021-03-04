# def foo():
#     buffer = []
#     for i in range(2):
#         print('foo():printが評価されました')
#         buffer.append('foo')
#     return buffer

# def main():
#     for x in foo():
#         print('main():' + x)

# main()
# foo():printが評価されました
# foo():printが評価されました
# main():foo
# main():foo

def bar():
    for i in range(2):
        print('bar():printが評価されました')
        yield 'bar'

def main():
    for x in bar():
        print('main():' + x)

main()
# bar():printが評価されました
# main():bar
# bar():printが評価されました
# main():bar
