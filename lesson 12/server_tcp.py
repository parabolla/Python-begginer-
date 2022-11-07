import socket
import json
from threading import Event

event = Event()


def send():
    pass


def reception():
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 9999))
    server_sock.listen(5)

    while True:
        event.set()
        client_socker, addr = server_sock.accept()  # получаем от клиента(кортеж)
        request = client_socker.recv(1024)  # получение данных
        print(request.decode("utf-8"))
        print()
        print(addr)
        event.wait()
        client_socker.sendall(request)  # отправляем сообщение обратно
        client_socker.close()
        event.clear()


if __name__ == '__main__':
    reception()
