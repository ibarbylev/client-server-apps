"""Client script that sends/reads simple text messages to the server"""

from socket import socket, AF_INET, SOCK_STREAM

address = ('localhost', 10000)


def echo_client():
    """Communicate with server"""
    with socket(AF_INET, SOCK_STREAM) as sock:
        sock.connect(address)
        while True:
            # The message must not consist of an empty string or spaces
            msg = ''
            while msg.strip() == '':
                msg = input('Please enter your message: ')
            if msg == 'exit':
                break
            sock.send(msg.encode('utf-8'))
            data = sock.recv(1024).decode('utf-8')
            print(f"Answer: {data}")


if __name__ == '__main__':
    echo_client()
