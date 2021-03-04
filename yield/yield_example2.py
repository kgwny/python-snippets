from time import sleep
from itertools import islice

def very_heavy(s):
    # 3の倍数の時だけすごい重くなる
    if s % 3 == 0:
        sleep(s)
    return s

# 先行評価だと、全部評価してしまい非効率
def get_result():
    buffer = []
    for i in range(10):
        buffer.append(very_heavy(i))
    return buffer

# 遅延評価なら必要なだけしか評価されない
def get_lazy_result():
    for i in range(10):
        yield very_heavy(i)

get_result()[:5] # 実行時間は常に18秒
list(islice(get_lazy_result(),5)) # 実行時間は3秒
