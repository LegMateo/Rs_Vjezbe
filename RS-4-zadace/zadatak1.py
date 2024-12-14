import asyncio
import aiohttp
import time

# 1


async def fetch_users(session, i):
    print(i)
    data = await session.get("https://jsonplaceholder.typicode.com/users")
    res = await data.json()
    return (
        [user["name"] for user in res],
        [user["email"] for user in res],
        [user["username"] for user in res],
    )


async def main():
    async with aiohttp.ClientSession() as session:
        start = time.time()
        users = [asyncio.create_task(fetch_users(session, i)) for i in range(5)]
        result = await asyncio.gather(*users)
        end = time.time()

        print(f"Vrijeme:  {end - start:.2f}")

        for names, email, username in result:
            all_names = names
            all_email = email
            all_username = username

        print("Sva imena: ", all_names)
        print("Svi emailovi: ", all_email)
        print("Svi username: ", all_username)


asyncio.run(main())
