"""
1. Каждое из слов «разработка», «сокет», «декоратор» представить
в строковом формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать строковые представление
в формат Unicode и также проверить тип и содержимое переменных.
"""


def print_value_and_type(items: list):
    for item in items:
        print(item)
        print(type(item))
    print()


VAR_1 = 'разработка'
VAR_2 = 'сокет'
VAR_3 = 'декоратор'

STR_LIST = [VAR_1, VAR_2, VAR_3]

print_value_and_type(STR_LIST)

VAR_UNIC_1 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
VAR_UNIC_2 = '\u0441\u043e\u043a\u0435\u0442'
VAR_UNIC_3 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

UNIC_LIST = [VAR_UNIC_1, VAR_UNIC_2, VAR_UNIC_3]

print_value_and_type(UNIC_LIST)
