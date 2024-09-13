import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1) # Time waits for one second
    print("World")

# Running the coroutine
asyncio.run(say_hello())
