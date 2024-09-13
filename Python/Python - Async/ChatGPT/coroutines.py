import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates an I/O operation
    print("Data fetched!")


async def main():
    await fetch_data()

asyncio.run(main())
