class Dto:
    def __init__(self):
        self.column_id = 0
        self.column_name = ''
        self.column_amount = 0

    def set_dto(self, id: int, name: str, amount: int):
        self.column_id = id
        self.column_name = name
        self.column_amount = amount

dto_list = []

# listの要素へ設定するdtoはすべて固有のオブジェクトを使用すること
b1 = Dto()
b1.set_dto(1, 'note', 108)
dto_list.append(b1)

b2 = Dto()
b2.set_dto(2, 'pencil', 78)
dto_list.append(b2)

b3 = Dto()
b3.set_dto(3, 'eraser', 99)
dto_list.append(b3)

# ループ処理でlistから1件ずつdtoを抽出する
for i in range(len(dto_list)):
    print('id=',dto_list[i].column_id,'name=',dto_list[i].column_name,'amount=',dto_list[i].column_amount)
