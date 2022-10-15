"""Decorator-function with parameter"""

import time


def sleep(timeout):
    """Outer function passes parameter <timeout>"""
    def decorator(func):
        """Middle function as decorator"""
        def decorated(*args, **kwargs):
            """Inner function as wrapper"""

            time.sleep(timeout)
            res = func(*args, **kwargs)

            print(f'Function {func.__name__} is working...')
            return res
        return decorated
    return decorator


@sleep(3)
def factorial(param):
    """Calculate factorial"""
    if param <= 1:
        return 1
    else:
        return param * factorial(param - 1)


print('!!! Pay attention to how many times the decorator for the recursive function '
      'will be called !!!')
print(factorial(5))
print()
