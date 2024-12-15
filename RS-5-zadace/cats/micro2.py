from aiohttp import web
import aiohttp
import asyncio

app = web.Application()


async def filter_cats(request):
    data = await request.json()

    filtered = [fact for fact in data["facts"] if "cat" or "Cat" in fact]
    return web.json_response({"facts": filtered})


app.router.add_post("/facts", filter_cats)


web.run_app(app, port=8087)
