import asyncio
"""
Handling results of coroutines
that may not be available yet
"""

async def set_after(fut, delay, value):
    await asyncio.sleep(delay)
    fut.set_result(value)


async def main():
    loop = asyncio.get_running_loop()
    fut = loop.create_future()

    loop.create_task(set_after(fut, 1, 'Hello, world!'))

    result = await fut
    print(result)

asyncio.run(main())
