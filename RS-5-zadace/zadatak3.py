from aiohttp import web
from aiohttp.web import AppRunner
import asyncio, aiohttp


proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50},
]

narudzbe = []

app = web.Application()


async def svi_proizvodi(request):
    return web.json_response(proizvodi, status=200)


async def id_proizvod(request):
    data = request.match_info["id"]

    if data is None:
        return web.json_response(proizvodi, status=200)

    for proizvod in proizvodi:
        if proizvod["id"] == int(data):
            return web.json_response(proizvod, status=200)

    return web.json_response(
        {"error": "Proizvod s traženim ID-em ne postoji"},
        status=404,
    )


async def naruci_proizvod(request):

    data = await request.json()

    print(data["proizvod_id"])

    for proizvod in proizvodi:
        if proizvod["id"] == data["proizvod_id"]:
            narudzbe.append(data)
            return web.json_response([narudzbe], status=201)

    return web.json_response(
        {"error": "Proizvod s traženim ID-em ne postoji"},
        status=200,
    )


app.router.add_get("/proizvodi", svi_proizvodi)

app.router.add_get("/proizvodi/{id}", id_proizvod)

app.router.add_post("/narudzbe", naruci_proizvod)


async def start_server():

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "localhost", 8081)
    await site.start()
    print("Server running at http://localhost:8081")


async def main():

    await start_server()

    async with aiohttp.ClientSession() as session:
        data = {
            "proizvod_id": 2,
            "kolicina": 2,
            "naziv": "Mis",
        }

        print("Klijentska sesija otvorena")

        rezultat = await session.get("http://localhost:8081/proizvodi")
        rezultat_2 = await session.get("http://localhost:8081/proizvodi/1")
        rezultat_3 = await session.post("http://localhost:8081/narudzbe", json=data)

        print(await rezultat.text())
        print(await rezultat_2.text())
        print(await rezultat_3.text())


asyncio.run(main())

web.run_app
