import asyncio
"""
These tasks run concurrently, and the main coroutine
waits for both tasks to complete before finishing.
"""

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")


async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")


async def main():
    task1_coro = task1()
    task2_coro = task2()

    await asyncio.gather(task1_coro, task2_coro)

asyncio.run(main())
