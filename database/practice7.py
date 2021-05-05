# 複数のテーブルをJOINする場合
# 複数のテーブルをJOINする場合は、switchを使用してどのテーブルに結合するかを明示しなければなりません。
# http://stackoverflow.com/questions/22016778/python-peewee-joins-multiple-tables

query = (TimeTableItem
    .select(TimeTableItem, TimeTable, BusStop)
    .join(TimeTable, on = (TimeTableItem.timeTable << list(timetableids.keys())))
    .switch(TimeTableItem)
    .join(BusStop, on=(TimeTableItem.busStop == BusStop.id))
)
for r in query:
    print (r.busStop.stopName)
