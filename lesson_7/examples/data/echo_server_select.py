"""Echo server handling simultaneous multiple clients
using the select function
"""

from select import select
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


def read_requests(read_clients, all_clients):
    """Reading requests from the list of clients"""

    responses = {}

    for sock in read_clients:
        try:
            data = sock.recv(1024).decode('utf-8')
            responses[sock] = data
        except Exception as e:
            print(e)
            print(f"Клиент {sock.fileno()} {sock.getpeername()} отключился")
            sock.close()
            all_clients.remove(sock)

    return responses


def write_responses(requests, clients_write, all_clients):
    """Response to clients from which requests were made"""

    for sock in clients_write:
        if sock in requests:
            try:
                if requests[sock] == '':
                    raise Exception
                resp = requests[sock].upper()
                print(resp)
                sock.send(resp.encode('utf-8'))
            except Exception as e:
                print(e)
                # sock.fileno() - client socket file descriptor (small integer)
                # sock.getpeername() - ip-address and port of client's socket
                print(f"Client  {sock.fileno()} {sock.getpeername()} disconnected")
                all_clients.remove(sock)
                sock.close()


def mainloop():
    """Main client request processing loop"""

    address = ('', 10000)
    all_clients = []

    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        sock.bind(address)
        sock.listen(5)
        sock.settimeout(1)
        while True:
            try:
                conn, addr = sock.accept()
            except OSError as err:
                pass
            else:
                print(f"Connection request received from {str(addr)}")
                all_clients.append(conn)
            finally:
                wait = 0
                clients_read = []
                clients_write = []
                try:
                    clients_read, clients_write, errors = select(all_clients, all_clients, [], wait)
                    # print(clients_read)
                    # print(clients_write)
                except Exception as e:
                    print(e)

                requests = read_requests(clients_read, all_clients)
                print(requests)
                if requests:
                    # print(requests)
                    write_responses(requests, clients_write, all_clients)


print('Echo server started...')
mainloop()
