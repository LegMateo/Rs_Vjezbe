import asyncio


# 1
async def fetch_data():
    print("Dohvaćam podatke...")
    data = [data for data in range(1, 11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return data


async def main():
    rezultat = await fetch_data()
    print(rezultat)


asyncio.run(main())
