import os, sys

def guess_charset(data):
    f = lambda d, enc: d.decode(enc) and enc

    try: return f(data, 'utf-8')
    except: pass
    try: return f(data, 'shift-jis')
    except: pass
    try: return f(data, 'euc-jp')
    except: pass
    try: return f(data, 'iso2022-jp')
    except: pass
    return None

def conv(data):
    charset = guess_charset(data)
    u = data.decode(charset)
    return u.encode('utf-8')

for dirpath, dirs, files in os.walk(os.getcwd()):
    for fn in files:
        path = os.path.join(dirpath, fn)
        fobj = open(path)
        data = fobj.read()
        fobj.close()
        try:
            data = conv(data)
        except:
            print(path, "-> skip")
            continue
        fobj = open(path)
        fobj.write(data)
        fobj.close()
        print(path, "-> converted")
