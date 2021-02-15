import platform
 
# osの判定
pf = platform.system()
 
if pf == 'Windows':
    print('Windows')
elif pf == 'Darwin':
    print('Mac')
elif pf == 'Linux':
    print('Linux')
else:
    exit(1)
 