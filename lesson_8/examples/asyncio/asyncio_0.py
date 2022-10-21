import random


def func1():
    for x in range(10**10000):
        v = random.randint(0, x)
        print(v, end=' -- ')


def func2():
    for x in range(10**10000):
        v = random.randint(0, x)
        print(v)


def main():
    func1()
    func2()


if __name__ == '__main__':
    main()
