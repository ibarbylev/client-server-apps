"""Task: create output for each pair of values from functions
function1 and function2:
v1 --- v2
"""


import random


def func1():
    for x in range(10**10000):
        v1 = random.randint(0, x)
        print(v1, end=' -- ')


def func2():
    for x in range(10**10000):
        v2 = random.randint(0, x)
        print(v2)


def main():
    func1()
    func2()


if __name__ == '__main__':
    main()
