from aiohttp import web
import asyncio

app = web.Application()


async def pozdrav(request):
    await asyncio.sleep(4)
    return web.json_response({"message": "Pozdrav nakon 4 sekunde"})


app.router.add_get("/", pozdrav)


web.run_app(app, port=8082)
