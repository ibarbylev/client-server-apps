import asyncio
import time
import requests


URLS = ['http://google.com' for _ in range(50)]


async def get_code_response(url):
    print('before request')
    status = requests.get(url).status_code
    print(status)


async def main(urls: list):
    await asyncio.gather(*(get_code_response(url) for url in urls))

if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main(URLS))
    delta = time.perf_counter() - start
    print(f"Script executed in {delta:0.2f} seconds.")


