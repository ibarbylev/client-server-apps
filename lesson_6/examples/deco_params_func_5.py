"""Decorator-function with parameter"""

import time
import requests


def decorator(iters):
    """Outer function passes parameter <timeout>"""
    def real_decorator(func):
        """Middle function as decorator"""
        def wrapper(*args, **kwargs):
            """Inner function as wrapper"""
            total_time = 0
            for i in range(iters):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                delta = end - start
                total_time += delta
                print(f'#{i + 1}: {delta:.2f} sec')
            print(f'Average time: {total_time / iters:.2f} sec')
        return wrapper
    return real_decorator


@decorator(10)
def get_wp(url):
    """Getting request"""
    requests.get(url)


get_wp('https://google.com')
# x = decorator(10)(get_wp)('https://google.com')
# print(x.__name__)
