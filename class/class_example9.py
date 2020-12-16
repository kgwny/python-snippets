class Hoge:
    def __init__(self):
        self.name = ''
        self.age = 0
        self.job = ''
        self.list = ''

    def set_list(self):
        self.list = self.name + '(' + str(self.age) + ')' + '・' + self.job

    def print_list(self):
        print(self.list)

h = Hoge()
h.name = '太郎'
h.age = 20
h.job = '会社員'
h.set_list()
h.print_list()
# 太郎(20)・会社員
