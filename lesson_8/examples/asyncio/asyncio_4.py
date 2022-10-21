import aiohttp
import asyncio
import time


URLS = ['http://google.com' for _ in range(50)]


async def get_code_response(url):
    async with aiohttp.ClientSession() as session:
        print('before request')
        async with session.get(url) as resp:
            print(resp.status)


async def main(urls: list):
    await asyncio.gather(*(get_code_response(url) for url in urls))

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main(URLS))
    delta = time.perf_counter() - start
    print(f"Script executed in {delta:0.2f} seconds.")


