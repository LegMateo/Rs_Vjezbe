from aiohttp import web

app = web.Application()


async def kolicnik(requests):

    data = await requests.json()

    temp = [item["result"] for item in data]

    print(temp)

    if temp[0] > temp[1]:
        return web.json_response({"result": temp[0] / temp[1]})
    else:
        return web.json_response({"result": (temp[1] / temp[0])})


app.router.add_post("/kolicnik", kolicnik)


web.run_app(app, port=8085)
