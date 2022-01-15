"""
Логирование с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""

import sys
import logging

# Создать логер - регистратор верхнего уровня
# с именем basic
log = logging.getLogger('basic')

# Создать обработчик, который выводит сообщения в поток stderr
# обработчики позволяют переопределить поведение корневого регистратора - log
stream_hand = logging.StreamHandler(sys.stderr)
# выводит в поток сообщения с уровнем CRITICAL
stream_hand.setLevel(logging.DEBUG)

# Создать объект Formatter и задать формат сообщений
formatter = logging.Formatter("%(levelname)-10s %(asctime)s %(message)s")

# подключить объект Formatter к обработчику
stream_hand.setFormatter(formatter)

# Добавить обработчик к регистратору
log.addHandler(stream_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Передать сообщение обработчику
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическое общение')
