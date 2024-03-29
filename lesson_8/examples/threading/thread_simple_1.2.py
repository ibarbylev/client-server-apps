"""Простой поток"""

import time
from threading import Thread


def clock(interval):
    """Функция, которая может быть запущена в потоке"""

    while True:
        time.sleep(interval)
        print(interval)
        print(f"Текущее время: {time.ctime()}")
        break


THR1 = Thread(target=clock, args=(2, ))
THR2 = Thread(target=clock, args=(3, ))

"""
Обычно Python-приложение не завершается, пока работает хоть один его поток. 
Но есть особые потоки, которые не мешают закрытию программы и останавливается вместе с ней. 
Их называют демонами (daemons). Проверить, является ли поток демоном, можно методом isDaemon(). 
Если является, метод вернёт истину.
"""
print(f"Время запуска основной программы: {time.ctime()}")
start = time.time()
# THR1.daemon = True
THR1.start()
THR2.start()
THR1.join()
THR2.join()
end = time.time()
print(f"Время окончания основной программы: {time.ctime()}")
print(f'end-start = {end-start:0.2f}')

# все потоки начинаются одновременно
# сначала отрабатывает первый поток, затем второй
# основной поток ждёт их завершения
