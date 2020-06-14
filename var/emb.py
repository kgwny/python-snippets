import textwrap

text = '''\
    Who are you? > {user}
    Input your password > {pswd}
'''

var = textwrap.dedent(text).format(user="taro", pswd="pass").strip()
print(var)
