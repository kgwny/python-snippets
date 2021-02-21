try:
    raise Exception('Generate Exception')
except Exception as e:
    print('except')
else:
    print('else')
finally:
    print('finally')
