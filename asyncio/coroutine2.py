import asyncio

# 名称を付与して1からmaxまでカウントする
async def counter_coroutine(name, max):
    count = 0
    while count < max:
        count += 1
        print(f'{name}: {count}')
        # asyncio.sleepはコルーチンなのでawaitで完了を待つ
        await asyncio.sleep(1)
    return f'{name} complete'

# カウンターを3つ同時に呼び出す
counters = asyncio.gather(
    counter_coroutine('counter 1', 1),
    counter_coroutine('counter 2', 2),
    counter_coroutine('counter 3', 3),
)
# asynio.gatherの返り値はfuture
print(f'counters is {counters}') 

loop = asyncio.get_event_loop()
# loop.run_until_completeによりreturnで返却された値を取得する
result = loop.run_until_complete(counters) 
print(result)
loop.close()
