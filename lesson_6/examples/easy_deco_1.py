"""Простейший декоратор-функция"""

import time


def decorator(func):
    """Сам декоратор"""
    def wrapper():
        """Обертка"""
        print('Сейчас выполняется функция-обёртка')
        time.sleep(2)
        print(f'Это просто ссылка на экземпляр оборачиваемой функции: {func}')
        time.sleep(2)
        print('Выполняем оборачиваемую (исходную) функцию...')
        time.sleep(2)
        func()
        time.sleep(2)
        print('Выходим из обёртки')

    return wrapper


@decorator
def some_text():
    """Какая-то логика"""
    print('вычисления')


print(type(some_text), some_text.__name__)

#some_text = decorator(some_text)
#some_text()
