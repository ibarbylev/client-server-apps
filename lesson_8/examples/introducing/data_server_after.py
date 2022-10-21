"""Server receives messages from clients and sends responses"""

from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from select import select

with socket(AF_INET, SOCK_STREAM) as server_cock:
    server_cock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    server_cock.bind(('', 8007))
    server_cock.listen(1)
    server_cock.settimeout(1)
    client_sockets = []

    while True:
        try:
            client_sock, address = server_cock.accept()
        except OSError as e:
            print(e)
        else:
            client_sockets.append(client_sock)
        finally:
            for client_socket in client_sockets:
                for_read = []
                for_read, _, _ = select(client_sockets, [], [], 0)
                if for_read:
                    data = client_socket.recv(4096)
                    print(f"Message: {data.decode('utf-8')} was sent by the client {address})")
                MSG = 'Hi client!'
                client_socket.send(MSG.encode('utf-8'))

