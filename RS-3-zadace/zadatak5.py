import asyncio


async def secure_data(podaci):
    await asyncio.sleep(3)
    return {
        "prezime": podaci["prezime"],
        "broj_kartice": hash(str(podaci["broj_kartice"])),
        "CVV": hash(str(podaci["CVV"])),
    }


data = [
    {"prezime": "Legovic", "broj_kartice": 874568746578346, "CVV": 459},
    {"prezime": "Sincic", "broj_kartice": 12098346457364, "CVV": 922},
    {"prezime": "Kocijancic", "broj_kartice": 12345623545978334, "CVV": 448},
]


async def main():
    zadaci = [asyncio.create_task(secure_data(podaci)) for podaci in data]

    rezultati = await asyncio.gather(*zadaci)

    for rezultat in rezultati:
        print(rezultat)


asyncio.run(main())
