"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор». Проверить кодировку
созданного файла (исходить из того, что вам априори неизвестна кодировка этого файла!).
Затем открыть этот файл и вывести его содержимое на печать.
ВАЖНО: файл должен быть открыт без ошибок вне зависимости от того,
в какой кодировке он был создан!
"""

from chardet import detect

words = ['сетевое программирование', 'сокет', 'декоратор']
with open('test.txt', 'w') as file:
    for word in words:
        file.write(f'{word}\n')


with open('test.txt', 'rb') as file:
    encoding = detect(file.read())['encoding']
    file.seek(0)
    content = file.read().decode(encoding=encoding)
print(content)
