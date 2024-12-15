import aiohttp
import asyncio
import time


async def fetch_service(port):
    async with aiohttp.ClientSession() as session:
        response = await session.get(f"http://0.0.0.0:{port}")
        return await response.json()


async def main():

    # SEKVENCIJALNO
    start = time.time()

    response_sequence = await fetch_service(8081), await fetch_service(8082)

    print(f"Servisi: { response_sequence}")
    end = time.time()
    print(f"Vrijeme: { end - start}")

    # KONKURENTNO
    start = time.time()
    service_response = await asyncio.gather(fetch_service(8081), fetch_service(8082))
    end = time.time()
    print(f"Servisi: { service_response}")
    print(f"Vrijeme: { end - start}")


asyncio.run(main())
