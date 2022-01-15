"""
Логирование с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""

import logging

# Создать логер - регистратор верхнего уровня
# с именем app.main
log = logging.getLogger('app.main')

# Создать обработчик
file_hand = logging.FileHandler("app.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG
file_hand.setLevel(logging.DEBUG)

# Создать объект formatter и задать формат сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s ")

# подключить объект Formatter к обработчику
file_hand.setFormatter(formatter)

# Добавить обработчик к регистратору
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Передать сообщение обработчику
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическое общение')
