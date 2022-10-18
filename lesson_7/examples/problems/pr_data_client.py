"""The client sends a hello to the server and
receives a response from it
"""

from socket import socket, AF_INET, SOCK_STREAM

with socket(AF_INET, SOCK_STREAM) as client_sock:
    client_sock.connect(('localhost', 8007))
    while True:
        MSG = 'Hi, server!'
        client_sock.send(MSG.encode('utf-8'))
        DATA = client_sock.recv(4096)
        print(f"Response from the server: {DATA.decode('utf-8')} "
              f"{len(DATA)} bytes long")
