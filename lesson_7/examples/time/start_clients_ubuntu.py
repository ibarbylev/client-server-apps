"""
Служебный скрипт запуска/останова нескольких клиентских приложений
"""

import os
import signal
import subprocess
import sys
from time import sleep


PYTHON_PATH = sys.executable
BASE_PATH = os.path.dirname(os.path.abspath(__file__))


def get_subprocess(file_with_args):
    sleep(1)
    file_full_path = f"{PYTHON_PATH} {BASE_PATH}/{file_with_args}"
    args = ["gnome-terminal", "--disable-factory", "--", "bash", "-c", file_full_path]
    return subprocess.Popen(args, preexec_fn=os.setpgrp)


P_LIST = []
while True:
    TEXT_FOR_INPUT = "Запустить 5 клиентов (s) / Закрыть клиентов (x) / Выйти (q): "
    USER = input(TEXT_FOR_INPUT)

    if USER == "q":
        break
    elif USER == "s":

        P_LIST.append(get_subprocess("time_server_select.py"))

        for i in range(5):
            P_LIST.append(get_subprocess("time_client_random.py"))

    elif USER == "x":
        while P_LIST:
            victim = P_LIST.pop()
            os.killpg(victim.pid, signal.SIGINT)
