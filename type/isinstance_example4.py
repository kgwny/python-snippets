def type_condition(val):
    if isinstance(val, str):
        print('type is str')
    elif isinstance(val, int):
        print('type is int')
    else:
        print('type is not str or int')

type_condition('string')
# type is str

type_condition(100)
# type is int

type_condition([0, 1, 2])
# type is not str or int
