import socket
import json
from threading import Event
import threading

lock = threading.RLock()
event = Event()


def send():
    pass


def reception():
    server_sock = socket.socket()
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 9999))
    server_sock.listen(5)
    users = []

    while True:
        client_socker, addr = server_sock.accept()  # получаем от клиента(кортеж)
        request = client_socker.recv(1024)  # получение данных
        users.append(addr)
        print("Список подлючений {}".format(users))
        print(request.decode("utf-8"))
        print()
        print("здесь адресс {}".format(addr))
        for user in users:
            print(user)
            if user[0] != addr[0]:
                client_socker.sendto(request, user)

        # client_socker.sendall(request)  # отправляем сообщение обратно
        client_socker.close()


if __name__ == '__main__':
    reception()
