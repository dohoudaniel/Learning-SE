import asyncio

async def risky_operation():
    await asyncio.sleep(1)
    raise ValueError("An error occurred")


async def main():
    try:
        await risky_operation()
    except ValueError as e:
        print(f"Caught an error: {e}")

asyncio.run(main())
