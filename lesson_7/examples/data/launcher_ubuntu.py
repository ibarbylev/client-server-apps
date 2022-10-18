"""
It is a launcher for starting subprocesses for server and clients of two types: senders and listeners.
for more information:
https://stackoverflow.com/questions/67348716/kill-process-do-not-kill-the-subprocess-and-do-not-close-a-terminal-window
"""

import os
import signal
import subprocess
import sys
from time import sleep


PYTHON_PATH = sys.executable
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
CLIENTS_COUNT = 2


def get_subprocess(file_with_args):
    sleep(0.2)
    file_full_path = f"{PYTHON_PATH} {BASE_PATH}/{file_with_args}"
    args = ["gnome-terminal", "--disable-factory", "--", "bash", "-c", file_full_path]
    return subprocess.Popen(args, preexec_fn=os.setpgrp)


processes = []
while True:
    TEXT_FOR_INPUT = "Select action: q - quit, s - run server and clients, x - close all windows: "
    action = input(TEXT_FOR_INPUT)

    if action == "q":
        break
    elif action == "s":
        processes.append(get_subprocess("echo_server_select.py"))

        for i in range(CLIENTS_COUNT):
            processes.append(get_subprocess("echo_client_select.py"))

    elif action == "x":
        while processes:
            victim = processes.pop()
            os.killpg(victim.pid, signal.SIGINT)
