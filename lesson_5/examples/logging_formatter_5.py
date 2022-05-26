"""
Логирование с использованием модуля logging
Расширенная настройка: логирование значений переменных
"""

import logging

# Создать логер - регистратор верхнего уровня
# с именем app.main
log = logging.getLogger('app')

# Создать обработчик
file_hand = logging.FileHandler("app_2.log", encoding='utf-8')
# выводит сообщения с уровнем DEBUG
file_hand.setLevel(logging.DEBUG)

# Создать объект formatter и задать формат сообщений
formatter = logging.Formatter("%(asctime)s - %(levelname)-8s - %(message)s")

# подключить объект Formatter к обработчику
file_hand.setFormatter(formatter)

# Добавить обработчик к регистратору
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)


if __name__ == '__main__':
    # Передать сообщение обработчику
    PARAMS = {'host': 'www.python.org', 'port': 80}
    log.debug('Отладочная информация. Параметры подключения: %(host)s, %(port)d', PARAMS)
    log.info('Информационное сообщение. Параметры подключения: %(host)s, %(port)d', PARAMS)
    log.warning('Предупреждение. Параметры подключения: %(host)s, %(port)d', PARAMS)
    log.error(f'Ошибка. Параметры подключения: {PARAMS["host"]}, {PARAMS["port"]}')
    log.critical(f'Критическое общение. Параметры подключения: '
                 f'{PARAMS["host"]}, {PARAMS["port"]}')
