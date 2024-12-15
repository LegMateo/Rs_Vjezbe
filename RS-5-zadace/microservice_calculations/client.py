import asyncio
import aiohttp


async def zbroji(list):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://0.0.0.0:8083/zbroj", json=list)

        res = await response.json()
        return res


async def pomnozi(list):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://0.0.0.0:8084/umnozak", json=list)
        res = await response.json()
        return res


async def kolicnik(rezultat):
    async with aiohttp.ClientSession() as session:
        response = await session.post("http://0.0.0.0:8085/kolicnik", json=rezultat)
        res = await response.json()
        return res


async def main():

    list = [num for num in range(1, 11)]

    result = await asyncio.gather(zbroji(list), pomnozi(list))

    print(result)

    koli = await kolicnik(result)

    print(koli)


asyncio.run(main())
