try:
    # 意図的に例外をなげる
    raise SystemError('Error message')
except SystemError as e:
    print('SystemError')
    print(e)
