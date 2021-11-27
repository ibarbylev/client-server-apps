"""
Задача:
ПЕРЕД выполнением и ПОСЛЕ выполнения определёных функций
печатать заданный текст (одинаковый для всех функций)
-------------------------------------------------------
Способ вернуть настоящее имя и док-стринг для функции с декоратором
"""
from functools import wraps


def decorator(func):
    """Сам декоратор"""
    @wraps(func)
    def wrap(*args, **kwargs):
        """Обертка"""
        print('Операция ДО выполнения функции some_func()')
        print(f'Переданные аргументы: {args}, {kwargs}')
        print('-' * 50)
        func()
        print('-' * 50)
        print('Операция ПОСЛЕ выполнения функции some_func()')
    return wrap


@decorator  # == decorator(some_func) !!!
def some_func():
    """Какая-то логика"""
    print('Выполнение самой функции some_func()')
    main_info = "Важная информация!"
    return main_info


some_func(1, 2, a=3, b=4)

# ==========================================
print('=' * 50)
print('Имя функции some_func() в декораторам  @decorator:', some_func.__name__)
print('Док-стринг функции some_func() в декораторам  @decorator:', some_func.__doc__)


# ==========================================
# Но как теперь получить значение переменной main_info из функции some_func() ?

print('=' * 50)
print('main_info из функции some_func() ==', some_func())
