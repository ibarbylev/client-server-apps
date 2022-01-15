"""
Форматирование
"""

import sys
import logging

# Результат %()-9s соответствует
# операции {:9} когда вы используете функцию format(value)
# или f{value:9} когда вы используете функцию f-string

# длина слова
WORD = 'CRITICAL'
len(WORD)

# Правый отступ равен 9 - длина слово
# Таким образом, мы имеем 1 пробел между словом и решеткой
print('{:9} #text'.format(WORD))
print(f'{WORD:11} #text')

# Создать логер и сравнить функцию format() и конструктор Formatter()
log = logging.getLogger('my_logger')
stream_hand = logging.StreamHandler(sys.stdout)

FORMAT_3 = '%(levelname)-13s #text - %(message)s'
formatter = logging.Formatter(FORMAT_3)
stream_hand.setFormatter(formatter)

log.addHandler(stream_hand)
log.setLevel(logging.ERROR)

if __name__ == '__main__':
    # Передать сообщение обработчику
    log.debug('Отладочная информация')
    log.info('Информационное сообщение')
    log.warning('Предупреждение')
    log.error('Ошибка')
    log.critical('Критическое общение')

