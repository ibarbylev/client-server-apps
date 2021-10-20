"""
for more information:
https://stackoverflow.com/questions/67348716/kill-process-do-not-kill-the-subprocess-and-do-not-close-a-terminal-window
"""

import os
import signal
import subprocess
import sys
from time import sleep

PROCESS = []
PYTHON_PATH = sys.executable
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
print(PYTHON_PATH, BASE_PATH)

while True:
    ACTION = input('Выберите действие: q - выход, '
                   's - запустить сервер и клиенты, x - закрыть все окна: ')

    if ACTION == 'q':
        break
    elif ACTION == 's':
        PROCESS.append(subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c',
                                         f'{PYTHON_PATH} {BASE_PATH}/server.py'], preexec_fn=os.setpgrp))

        for i in range(2):
            sleep(1)
            PROCESS.append(subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c',
                                             f'{PYTHON_PATH} {BASE_PATH}/client.py -m send'],
                                            preexec_fn=os.setpgrp))
        for i in range(2):
            sleep(1)
            PROCESS.append(subprocess.Popen(['gnome-terminal', '--disable-factory', '--', 'bash', '-c',
                                             f'{PYTHON_PATH} {BASE_PATH}/client.py -m listen'],
                                            preexec_fn=os.setpgrp))
    elif ACTION == 'x':
        while PROCESS:
            VICTIM = PROCESS.pop()
            os.killpg(VICTIM.pid, signal.SIGINT)

