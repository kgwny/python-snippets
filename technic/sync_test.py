import asyncio
import websockets
import concurrent.futures
import cv2
import time

# no test

# 同期処理
def th2():
    while True:
        print('-')
        time.sleep(0.1)

# 同期処理
def th():
    # 並列実行スレッド内部でさらに同期的なスレッド起動　　　　　　　　　　　　　　
    asyncio.ensure_future(loop.run_in_executor(exec, th2))
    # 普通の処理...

# 非同期処理コルーチン
async def ws_handler(ws, path):
    async for msg in ws:
        print('ws_svr > Received from client:', msg)
        await ws.send('pong')

if __name__ == '__main__':
    # 同期処理の並列実行準備
    exec = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    # 非同期処理設定
    ws_server = websockets.serve(ws_handler, '123.456.789.1', 8081)
    loop = asyncio.get_event_loop()
    # 同期処理の実行予約
    asyncio.ensure_future(loop.run_in_executor(exec, th))
    # 非同期処理実行ループ
    loop.run_until_complete(ws_server)
    loop.run_forever()
