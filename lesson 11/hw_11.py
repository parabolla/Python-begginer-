import threading
import time
from threading import Event

lock = threading.RLock()
event = Event()


class Writer1(threading.Thread):
    def __init__(self, interval, daemon=True):
        super().__init__()
        self.interval = interval
        self.daemon = daemon

    def run(self):
        while True:
            event.set()  # ждем выполнения первого писателя
            lock.acquire()  # блокируем
            file = open("txt.txt", "a")
            file.write("строка2")
            print("первый автор отписался")
            file.close()
            lock.release()  # разблокировка
            time.sleep(self.interval)


class Writer2(threading.Thread):
    def __init__(self, interval, daemon=True):
        super().__init__()
        self.interval = interval
        self.daemon = daemon

    def run(self):
        while True:
            event.set()  # ждем выполнения второго писателя
            lock.acquire()
            file = open("txt.txt", "a")
            file.write("строка3")
            print("второй автор отписался")
            file.close()
            lock.release()
            time.sleep(self.interval)


class Readers(threading.Thread):
    def __init__(self, daemon=True):
        super().__init__()
        self.daemon = daemon

    def run(self):
        while True:
            event.wait()  # после писателей, читаем текст
            event.set()
            lock.acquire()
            file = open("txt.txt", "r")
            print("мы все прочитали")
            file.close()
            lock.release()
            event.clear()


if __name__ == "__main__":
    t1 = Writer1(1)
    t2 = Writer2(1)
    r = Readers()
    t1.start()
    t2.start()
    r.start()
    time.sleep(5)  # количетсво записей
