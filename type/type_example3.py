def type_condition(val):
    if type(val) is str:
        print('type is str')
    elif type(val) is int:
        print('type is int')
    else:
        print('type is not str or int')

type_condition('string')
# type is str

type_condition(100)
# type is int

type_condition([0, 1, 2])
# type is not str or int
