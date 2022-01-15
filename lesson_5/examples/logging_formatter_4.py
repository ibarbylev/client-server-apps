"""
Логирование с использованием модуля logging
Расширенная настройка. Форматирование, обработчики
"""

import sys
import logging

# Создать логер - регистратор верхнего уровня
# с именем app
log = logging.getLogger('app')
# Установить уровень важности
log.setLevel(logging.INFO)

# Создать обработчик, который выводит сообщения с уровнем CRITICAL в поток stderr
stream_hand = logging.StreamHandler(sys.stderr)
stream_hand.setLevel(logging.INFO)

# Создать обработчик, который выводит сообщения в файл
file_hand = logging.FileHandler('app_4.log', encoding='utf-8')
file_hand.setLevel(logging.ERROR)

# Создать объект formatter и задать формат сообщений
formatter = logging.Formatter("%(asctime)s %(levelname)-8s - %(message)s ")

# подключить объект Formatter к обработчикам
stream_hand.setFormatter(formatter)
file_hand.setFormatter(formatter)

# Добавить обработчики к регистратору
log.addHandler(stream_hand)
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Передать сообщение обработчику
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическое общение')
