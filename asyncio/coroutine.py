import asyncio

# 1からmaxまでカウント
async def counter_coroutine(max):
    count = 0
    while count < max:
        count += 1
        print(count)
        # asyncio.sleepはコルーチンなのでawaitで完了を待つ
        await asyncio.sleep(1) 
    return 'complete'

# コルーチン関数の返却値はコルーチンオブジェクト
counter = counter_coroutine(3)
print(f'counter is {counter}')
loop = asyncio.get_event_loop()

# コルーチン関数がreturnで返却した値はloop.run_until_completeの返却値となる
result = loop.run_until_complete(counter)
print(result)

loop.close()
