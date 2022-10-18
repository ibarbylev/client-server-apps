"""A time server that handles "simultaneously" multiple clients.
Client processing is done by the select function
"""

import time
import select
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def new_listen_socket(address):
    """Initiating a server socket"""
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sock.bind(address)
    sock.listen(5)
    # проверяем есть ли новые клиенты
    # проверяем есть ли данные
    sock.settimeout(1)
    return sock


def mainloop():
    """Main client request processing loop"""
    address = ('', 8888)
    all_clients = []
    sock = new_listen_socket(address)

    while True:
        try:
            conn, addr = sock.accept()
        except OSError as err:
            print(f'OSError code on the server side is : {err.errno}')
            # The error number returns None because it's just a timeout
            pass
        else:
            print(f"Received a connection request from {str(addr)}")
            # Add a new client to the list all_clients
            all_clients.append(conn)
        finally:
            clients_write = []
            try:
                _, clients_write, _ = select.select([], all_clients, [], 0)

            except Exception as e:
                print(e)
                pass

            for client in clients_write:
                # get time value
                time_str = time.ctime(time.time()) + "\n"
                try:
                    # and sent time value to client
                    client.send(time_str.encode('utf-8'))

                except Exception as e:
                    print(e)
                    # client disconnected
                    all_clients.remove(client)
                    client.close()


print('Echo server started...')
mainloop()
