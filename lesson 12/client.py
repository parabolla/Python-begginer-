import socket
import json
import threading
import time

from datetime import datetime

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
lock = threading.RLock()

port = int(input("enter your port: "))
name = input(str("Введите имя: "))
sock = socket.socket()
sock.connect(('localhost', port))

while True:
    # serversock = socket(AF_INET, SOCK_STREAM)
    mess = input("Введите сообщение: ")
    lock.acquire()
    json_str = {
        "action": "msg_from_chat",
        "time": current_time,
        "message": mess,
        "user":
            {"name": name,
             "status": "online"}
    }
    json_str = json.dumps(json_str)
    sock.send(json_str.encode("utf-8"))
    lock.release()
    time.sleep(1)
    lock.acquire()
    data = sock.recv(1024)
    lock.release()
    time.sleep(1)
    # if
    sock.close()
