"""
Логгирование с использованием модуля logging
асширенная настройка. Форматирование, обработчики
"""

import logging

# Создать логгер - регистратор верхнего уроовня
# с именем app.main
LOG = logging.getLogger('app')

# Создать обработчик
FILE_HANDLER = logging.FileHandler("app_2.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG
FILE_HANDLER.setLevel(logging.DEBUG)

# Создать объект Formatter
# Определить формат сообщений
FORMATTER = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s")

# подключить объект Formatter к обработчику
FILE_HANDLER.setFormatter(FORMATTER)

PARAMS = {'host': 'www.python.org', 'port': 80}

# Добавить обработчик к регистратору
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(logging.DEBUG)


if __name__ == '__main__':
    # Передать сообщение обработчику
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')
    LOG.warning('Предупреждение')
    LOG.error('Ошибка')
    LOG.critical('Критическое общение')
