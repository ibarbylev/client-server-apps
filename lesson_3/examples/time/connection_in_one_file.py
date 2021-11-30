from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import time

SERV_SOCK = socket(AF_INET, SOCK_STREAM)
SERV_SOCK.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
SERV_SOCK.bind(('localhost', 8888))
SERV_SOCK.listen()
print('SERV_SOCK : ', SERV_SOCK)


CLIENT_SOCK = socket(AF_INET, SOCK_STREAM)
CLIENT_SOCK.connect(('localhost', 8888))
print('CLIENT_SOCK : ', CLIENT_SOCK)

CLIENT_SOCK_SERV, ADDR = SERV_SOCK.accept()
print('CLIENT_SOCK_2 : ', CLIENT_SOCK_SERV)
print(f'Получен запрос на соединение от клиента с адресом и портом: {ADDR}')
TIMESTR = time.ctime(time.time()) + "\n"
CLIENT_SOCK_SERV.send(TIMESTR.encode('utf-8'))
TIME_BYTES = CLIENT_SOCK.recv(1024)
print(f"Текущее время: {TIME_BYTES.decode('utf-8')}")

time.sleep(1)
TIMESTR = time.ctime(time.time()) + "\n"
CLIENT_SOCK.send(TIMESTR.encode('utf-8'))
TIME_BYTES = CLIENT_SOCK_SERV.recv(1024)
print(f"Текущее время: {TIME_BYTES.decode('utf-8')}")

CLIENT_SOCK.close()
