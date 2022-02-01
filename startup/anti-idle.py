import asyncio

async def continuous_print():
    while True:
        print('I am Alive!!')
        await asyncio.sleep(300)
    return False

asyncio.run(continuous_print())
