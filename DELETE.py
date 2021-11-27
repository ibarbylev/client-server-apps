def func(a):
    y = a

    def wrap(x):
        return x + y
    return wrap


add_2 = func(2)
print(add_2(2))
print(add_2.__name__)
