"""
It is a launcher for starting subprocesses for server and clients of two types: senders and listeners.
for more information:
https://stackoverflow.com/questions/67348716/kill-process-do-not-kill-the-subprocess-and-do-not-close-a-terminal-window
"""

import os
import signal
import subprocess
import sys
import time
from time import sleep


PYTHON_PATH = sys.executable
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CLIENTS_COUNT = 3


def get_subprocess(file_with_args):
    sleep(0.2)
    file_full_path = f"{PYTHON_PATH} {BASE_PATH}/{file_with_args}"
    args = ["gnome-terminal", "--disable-factory", "--", "bash", "-c", file_full_path]
    return subprocess.Popen(args, preexec_fn=os.setpgrp)


processes = []
while True:
    question = f"Запустить {CLIENTS_COUNT} клиентов (s) / Закрыть клиентов (x) / Выйти (q): "
    choice = input(question)

    if choice == "q":
        break
    elif choice == "s":

        processes.append(get_subprocess("time_server_select.py"))
        time.sleep(0.2)
        for i in range(CLIENTS_COUNT):
            processes.append(get_subprocess("time_client_random.py"))

        print(f'Число запущенных клиентских скриптов: {CLIENTS_COUNT}')

    elif choice == "x":
        while processes:
            victim = processes.pop()
            os.killpg(victim.pid, signal.SIGINT)
