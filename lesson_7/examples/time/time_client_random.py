"""Client program that endlessly requests the current time"""

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as client_sock:
    client_sock.connect(('localhost', 8888))

    while True:
        time_bytes = client_sock.recv(1024)
        print(f"Текущее время: {time_bytes.decode('utf-8')}")

