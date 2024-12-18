from cctv import CCTV_frame
import asyncio
import random
import aiohttp


async def simulate_movement(seconds, frame_rate):
    lista = []
    for _ in range(seconds * frame_rate):
        lista.append((random.uniform(-100, 100), random.uniform(-100, 100)))

    return lista


async def update_camera_location(instance, x, y):
    instance.update_location(x, y)

    return instance.info()


async def main():

    instance = CCTV_frame(12112, 56, 30, 30, True, 50, "192.168.1.1")
    instance.info()

    simulation = await simulate_movement(5, 30)

    tasks = [asyncio.create_task(simulate_movement(i, 30)) for i in range(1, 6)]

    positions = await asyncio.gather(*tasks)

    print(positions)

    # count = 0
    # for i in positions:
    # for _ in i:
    # count += 1

    count = sum(len(i) for i in positions)
    print(count)

    updated_info = await update_camera_location(instance, 11, 2)

    print(updated_info)

    normalised_positions = []
    for j in positions:
        for i in j:
            normalised_positions.append(i)

    first_50_positions = normalised_positions[0:50]

    print(first_50_positions)

    tasks = [
        asyncio.create_task(update_camera_location(instance, i[0], i[1]))
        for i in first_50_positions
    ]

    result = await asyncio.gather(*tasks)

    async with aiohttp.ClientSession() as session:
        response = await session.post("http://0.0.0.0:8080/cctv", json=result)
        print(await response.json())


asyncio.run(main())
