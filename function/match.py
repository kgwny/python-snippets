from fnmatch import fnmatch

class glob_list(list):
    def __contains__(self, value):
        for pattern in self:
            if fnmatch(value, pattern):
                return True
        return False

# ファイル名が hoge.txt か piyo.md にマッチしてるかチェック
l = glob_list(['??ge.txt', '?iyo.md'])

print(True) if 'hoge.txt' in l else print(False)
print(True) if 'hige.txt' in l else print(False)
print(True) if 'piyo.md' in l else print(False)
print(True) if 'iiyo.md' in l else print(False)

# assert 'hoge.txt' in l
# assert 'hige.txt' in l
# assert 'piyo.md' in l
# assert 'iiyo.md' in l
