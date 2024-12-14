import asyncio
import aiohttp
import time


# 3
async def get_dog_fact(session):
    res = await session.get("https://dogapi.dog/api/v2/facts")
    results = await res.json()

    return [fact["attributes"]["body"] for fact in results["data"]]


async def get_cat_fact(session):
    data = await session.get("https://catfact.ninja/fact")
    results = await data.json()

    return [results["fact"]]


async def mix_facts(dog_list, cat_list):

    return [
        ("Dog", (dog[0])) if len(dog[0]) > len(cat[0]) else ("Cat", (cat[0]))
        for dog, cat in zip(dog_list, cat_list)
    ]


async def main():
    async with aiohttp.ClientSession() as session:

        dogs = [get_dog_fact(session) for _ in range(5)]
        cats = [get_cat_fact(session) for _ in range(5)]

        dog_cat_facts = await asyncio.gather(*dogs, *cats)

        # print(dog_cat_facts)

        dog_list = dog_cat_facts[:5]
        cat_list = dog_cat_facts[5:]

        mixed = await mix_facts(dog_list, cat_list)
        # print("DOG: ", dog_list)
        # print("CAT: ", cat_list)

        print("Mixane činjenice o psima i mačkama: ", mixed)


asyncio.run(main())
