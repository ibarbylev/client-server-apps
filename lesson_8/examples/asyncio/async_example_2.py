import asyncio
import aiohttp

URLS = ['http://google.com' for _ in range(5)]


async def get_code_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print(resp.status)
            # print(await resp.text())


async def main(urls: list):
    x = await asyncio.gather(*(get_code_response(url) for url in URLS))

if __name__ == "__main__":
    import time
    s = time.perf_counter()
    print('s = ', s)
    asyncio.run(main(URLS))
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")

