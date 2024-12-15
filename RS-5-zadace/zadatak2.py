from aiohttp import web

# 3
app = web.Application()

korisnici = [
    {"ime": "Ivo", "godine": 25},
    {"ime": "Ana", "godine": 17},
    {"ime": "Marko", "godine": 19},
    {"ime": "Maja", "godine": 16},
    {"ime": "Iva", "godine": 22},
]


async def samo_punoljetni(requests):
    return web.json_response(
        [
            {"ime": korisnik["ime"], "godine": korisnik["godine"]}
            for korisnik in korisnici
            if korisnik["godine"] >= 18
        ]
    )


app.router.add_get("/punoljetni", samo_punoljetni)


web.run_app(app, port=8082)
