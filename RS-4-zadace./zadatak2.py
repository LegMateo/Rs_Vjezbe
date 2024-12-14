import asyncio
import time
import aiohttp


# 2
async def get_cat_fact(session):
    data = await session.get("https://catfact.ninja/fact")
    res = await data.json()
    return res


async def filter_cat_facts(results):
    return [fact["fact"] for fact in results if "cat" or "Cat" in fact["fact"]]


async def main():
    async with aiohttp.ClientSession() as session:

        task = [get_cat_fact(session) for _ in range(20)]

        results = await asyncio.gather(*task)

        print(results)

        cats = await filter_cat_facts(results)
        print(cats)


asyncio.run(main())
