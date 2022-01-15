"""
Простейшее логирование
"""

import logging

# Создаём объект-логер с именем app.main
log = logging.getLogger('app.main')

# Создаём объект форматирования:
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s ")

# Создаём файловый обработчик логирования (можно задать кодировку):
file_hand = logging.FileHandler("app.main.log", encoding='utf-8')
# fh.setLevel(logging.DEBUG)
file_hand.setFormatter(formatter)

# Добавляем в логер новый обработчик событий и устанавливаем уровень логирования
log.addHandler(file_hand)
log.setLevel(logging.DEBUG)

if __name__ == '__main__':
    # Создаём потоковый обработчик логирования (по умолчанию sys.stderr):
    stream_hand = logging.StreamHandler()
    # console.setLevel(logging.DEBUG)
    stream_hand.setFormatter(formatter)
    log.addHandler(stream_hand)
    # В логирование передаем имя текущей функции и имя вызвавшей функции
    log.debug('Отладочное сообщение')
