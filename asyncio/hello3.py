import asyncio
import time

async def hello_world():
    time.sleep(5)
    print("Hello World!")

async def call_hello_world():
    await hello_world()

loop = asyncio.get_event_loop()
loop.run_until_complete(call_hello_world())
