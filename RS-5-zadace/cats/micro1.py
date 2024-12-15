from aiohttp import web
import aiohttp
import asyncio

app = web.Application()


async def fact_cat():
    async with aiohttp.ClientSession() as session:
        result = await session.get("https://catfact.ninja/fact")
        res = await result.json()
        return res


async def get_cats(request):
    num = int(request.match_info.get("num", 1))
    tasks = [asyncio.create_task(fact_cat()) for _ in range(num)]
    data = await asyncio.gather(*tasks)

    return web.json_response(
        {"facts": [fact["fact"] for fact in data], "message": "OK", "received_num": num}
    )


app.router.add_get("/cats/{num}", get_cats)


web.run_app(app, port=8086)
