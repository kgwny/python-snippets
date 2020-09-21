import functools

# open
open_utf_8 = functools.partial(open, encoding="utf-8")
# read
r_open_utf_8 = functools.partial(open_utf_8, mode="r")
# write
w_open_utf_8 = functools.partial(open_utf_8, mode="w")

with w_open_utf_8('./tmp/tmp.txt') as wf:
    wf.write("Hello World!")
