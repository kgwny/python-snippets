import asyncio
import time

async def hello_world():
    time.sleep(5)
    print("Hello World!")

async def call_hello_world():
    print("start")
    await hello_world()
    print("end")

loop = asyncio.get_event_loop()

for num in [1, 2, 3, 4, 5]:
    loop.run_until_complete(call_hello_world())
    print(str(num))
