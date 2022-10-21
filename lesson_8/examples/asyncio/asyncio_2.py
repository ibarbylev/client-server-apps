""" A coroutine is a specialized version of a Python generator function.
Coroutine is a function that can suspend its execution before reaching return,
and it can indirectly pass control to another coroutine for some time.
"""


import asyncio
import time


async def count():
    print('First line')
    await asyncio.sleep(1)
    print('Second line')


async def main():
    await asyncio.gather(count(), count(), count())


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    delta = time.perf_counter() - start
    print(f"Script executed in {delta:0.2f} seconds.")

