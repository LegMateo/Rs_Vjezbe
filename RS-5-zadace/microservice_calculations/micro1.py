import asyncio
from aiohttp import web

app = web.Application()


async def zbroji(request):
    data = await request.json()

    if not isinstance(data, list):
        return web.json_response({"message": "Brojevi nisu proslijedeni"}, status=404)

    if not data:
        return web.json_response({"message": "Lista je prazna"}, status=404)

    print(data)

    total = sum(data)

    return web.json_response({"operation": "sum", "result": total})


app.router.add_post("/zbroj", zbroji)


web.run_app(app, port=8083)
