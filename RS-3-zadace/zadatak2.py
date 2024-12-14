import asyncio


# 2
async def fetch_web_1():
    print("Dohvaćam podatke...")
    data = [
        {"ime": "Ivan", "prezime": "Matic", "broj": "099455667"},
        {"ime": "Marko", "prezime": "Maric", "broj": "098782445"},
    ]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni.")
    return data


async def fetch_web_2():
    print("Dohvaćam podatke...")
    data = [
        {"proizvod": "Banana", "kolicina": 1, "sifra": "55487384683648"},
        {"proizvod": "Jabuka", "kolicina": 3, "broj": "758748888484833"},
    ]
    await asyncio.sleep(5)
    print("Podaci dohvaćeni.")
    return data


async def main():

    rezultat = await asyncio.gather(fetch_web_1(), fetch_web_2())

    print(rezultat)


asyncio.run(main())
