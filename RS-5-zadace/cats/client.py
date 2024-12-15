import asyncio
import aiohttp


async def get_cats(num):
    async with aiohttp.ClientSession() as session:
        result = await session.get(f"http://0.0.0.0:8086/cats/{num}")
        res = await result.json()
        return res


async def filter_cats(data):
    async with aiohttp.ClientSession() as session:
        result = await session.post("http://0.0.0.0:8087/facts", json=data)
        res = await result.json()
        return res


async def main():
    res = await get_cats(5)

    cats = await filter_cats(res)

    # print(res)

    print(cats)


asyncio.run(main())
