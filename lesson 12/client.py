import socket
import json
import threading
import time
from threading import Event
from datetime import datetime

event = Event()

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
lock = threading.RLock()

port = int(input("enter your port: "))
name = input(str("Введите имя: "))

while True:
    sock = socket.socket()
    sock.connect(("localhost", port))

    mess = input("Введите сообщение: ")
    json_str = {
        "action": "msg_from_chat",
        "time": current_time,
        "message": mess,
        "user":
            {"name": name,
             "status": "online"}
    }
    print("я тут")
    json_str = json.dumps(json_str)
    sock.send(json_str.encode("utf-8"))
    time.sleep(0.2)
    print("sleep")
    data = sock.recv(1024)
    print(data.decode())
    sock.close()
