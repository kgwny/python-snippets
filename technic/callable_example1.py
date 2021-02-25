# https://docs.python.org/3/library/typing.html#callable
from typing import Callable

# 関数の引数/返り値型の定義をまとめたもの
# コールバック関数のように関数が引数となる場合、また関数を返すような場合に利用する

# Callable([引数型], 返り値型)
# 以下は、関数を引数に取るfeeder/async_queryについて、
# Callableでアノテーションを行っている例となります

def feeder(get_next_item: Callable[[], str]) -> None:
    print('aaa')

def async_query(on_success: Callable[[int], None],
                on_error: Callable[[int, Exception], None]) -> None:
    print('bbb')
