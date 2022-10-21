"""Task: create output for each pair of values from functions
function1 and function2:
v1 --- v2
"""
import random


def func1():
    for x in range(10**10000):
        v1 = random.randint(0, x)
        yield v1


def func2():
    for x in range(10**10000):
        v2 = random.randint(0, x)
        yield v2


def main():
    v1 = func1()
    v2 = func2()
    while True:
        try:
            print(next(v1), end=' -- ')
            print(next(v2))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()
