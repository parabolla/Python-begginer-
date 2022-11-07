import socket
import datetime
import threading
import time
import json

lock = threading.RLock()

server_socket = socket.socket()
server_socket.bind(("localhost", 6666))
server_socket.listen(10)  # Делает сервером(слушает порты)

while True:
    conn, addr = server_socket.accept()  # подключениек клиента
    lock.acquire()
    request = conn.recv(1024)  # размер передоваемого файла
    # json_str = {
    #     "action": "msg_from_chat",
    #     "time": time
    #     "message" : request
    #     "user" :
    # }
    print(request.decode())
    lock.release()
    time.sleep(0.2)
    lock.acquire()
    conn.sendall("back send".encode())
    lock.release()
    time.sleep(0.2)
    conn.close()
