def func1():
    for x in range(10**10000):
        yield x


def func2():
    for x in range(10**10000):
        yield x * (-1)


def main():
    f1 = func1()
    f2 = func2()
    try:
        while True:
            print(next(f1), end=' -- ')
            print(next(f2))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    main()
