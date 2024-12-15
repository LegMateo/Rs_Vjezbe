from aiohttp import web

app = web.Application()


async def pomnozi(requests):

    data = await requests.json()

    if not isinstance(data, list):
        return web.json_response({"message": "Brojevi nisu proslijedeni"}, status=404)

    if not data:
        return web.json_response({"message": "Lista je prazna"}, status=404)

    print(data)

    product = 1
    for item in data:
        product = product * item

    return web.json_response({"operation": "multyply", "result": product})


app.router.add_post("/umnozak", pomnozi)


web.run_app(app, port=8084)
