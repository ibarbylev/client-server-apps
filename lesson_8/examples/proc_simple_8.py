"""
Мультипроцессинг с функцией
subprocess vs multiprocessing:
https://stackoverflow.com/questions/13606867/what-is-the-difference-between-multiprocessing-and-subprocess
"""

import time
import multiprocessing


def clock(interval):
    """Простая функция"""
    while True:
        print(f"The time is {time.ctime()}")
        time.sleep(interval)


if __name__ == "__main__":
    PROC = multiprocessing.Process(target=clock, args=(1, ))
    PROC.start()
