from aiohttp import web

# 1, 2
app = web.Application()

proizvodi = [
    {"naziv": "Banana", "cijena": 2, "kolicina": 62},
    {"naziv": "Pekmez", "cijena": 4, "kolicina": 12},
    {"naziv": "Kava", "cijena": 7, "kolicina": 19},
]


async def dohvati_proizvode(requests):
    return web.json_response(proizvodi, status=200)


async def dodaj_proizvode(requests):
    data = await requests.json()
    print(data)
    proizvodi.append(data)
    return web.json_response(proizvodi, status=201)


app.router.add_get("/proizvodi", dohvati_proizvode)
app.router.add_post("/proizvodi", dodaj_proizvode)

web.run_app(app, port=8081)
