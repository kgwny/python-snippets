import asyncio
import time

async def sleeping(time_sec):
    loop = asyncio.get_event_loop()
    print(f'start:  wait {time_sec} sec')
    await loop.run_in_executor(None, time.sleep, time_sec)
    print(f'finish: wait {time_sec} sec')

def main():
    loop = asyncio.get_event_loop()

    print('\n単一実行')
    loop.run_until_complete(sleeping(10))

    print('\n並列実行')
    gather = asyncio.gather(
        sleeping(5),
        sleeping(1),
        sleeping(8),
        sleeping(3),
        sleeping(4)
    )
    loop.run_until_complete(gather)

if __name__ == '__main__':
    main()
