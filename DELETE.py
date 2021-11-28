"""
Добавить параметр в декоратор класса
https://stackoverflow.com/questions/7492068/python-class-decorator-arguments

What is the difference between __init__ and __call__?
https://stackoverflow.com/questions/9663562/what-is-the-difference-between-init-and-call
"""
import functools


class Log:
    """Класс-декоратор"""
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func
        self.param = 0

    def __call__(self, *args, **kwargs):
        """Обертка"""
        res = self.func(*args, **kwargs)
        print(f'log: {self.func.__name__}({args}, {kwargs}) = {res}')
        return res


@Log
def my_func(val_1, val_2):
    """Вычисление"""
    return val_1 ** val_2


# print('-- Функции с декораторами --')
# my_func(4, 5)

# другой подход применения декоратора к функции func2 = Log()(func2)
# func2 = Log()(my_func)
# func2(4, 5)
Log(my_func(4, 5))
