"""
Задача:
ПЕРЕД выполнением и ПОСЛЕ выполнения определённых функций
печатать заданный текст (одинаковый для всех функций)
-------------------------------------------------------
Синтаксический сахар @decorator
"""


def decorator(func):
    """Сам декоратор"""
    def wrap():
        """Обертка"""
        print('Операция ДО выполнения функции some_func()')
        print('-' * 50)
        print(f'Имя функции some_func() внутри декоратора: {func.__name__}')
        func()
        print('-' * 50)
        print('Операция ПОСЛЕ выполнения функции some_func()')
    return wrap


@decorator  # == decorator(some_func) !!!
def some_func():
    """Какая-то логика"""
    print('Выполнение самой функции some_func()')


some_func()

# ==========================================
# Но какое имя у новой функции some_func() с декоратором @decorator ?


# print('=' * 50)
# print('Имя функции some_func() c декораторам  @decorator:', some_func.__name__)
# print('Док-стринг функции some_func() c декораторам  @decorator:', some_func.__doc__)

# Это конечно плохо.
# Но зато это даёт нам определённые преимущества:
# значит с помощью параметров функции wrap()
# в нашу конструкцию можно передавать дополнительные аргументы!
