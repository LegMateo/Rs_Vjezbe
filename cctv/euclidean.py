from aiohttp import web
import uuid

app = web.Application()


async def udaljenost(request):
    data = await request.json()

    for list in data:
        distance = (list[1] - list[0]) ** 2
        return distance

    return web.json_response({data})


app.router.add_post("/euclidean", udaljenost)


if __name__ == "__main__":
    web.run_app(app, port=8091)
