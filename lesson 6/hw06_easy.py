# Задача-1:
# Следующая программа написана верно, однако содержит места потенциальных ошибок.
# используя конструкцию try добавьте в код обработку соответствующих исключений.
# Пример.
# Исходная программа:
def avg(a, b):
    return (a * b) ** 0.5


try:
    a = float(input("a = "))
    b = float(input("b = "))
    c = avg(a, b)
    print("Среднее геометрическое = {:.2f}".format(c))
except ValueError:
    print("неверный формат данных, введите int or float")

# ПРИМЕЧАНИЕ: Для решения задач 2-4 необходимо познакомиться с модулями os, sys!
# СМ.: https://pythonworld.ru/moduli/modul-os.html, https://pythonworld.ru/moduli/modul-sys.html

# Задача-2:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os, sys

for i in range(1, 10):
    try:
        os.mkdir("dir_{}".format(i))
    except FileExistsError:
        print("Папка с именем {} уже создана".format("dir_{}".format(i)))
    try:
        os.rmdir("dir_{}".format(i))
    except FileNotFoundError:
        print("Папка с именем {} уже удаленная или отсутсвтует".format("dir_{}".format(i)))

# Задача-3:
# Напишите скрипт, отображающий папки текущей директории.
import os

print("Все папки:", os.listdir(path="/"))

# Задача-4:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import shutil

shutil.copyfile('hw06_easy.py', 'hw06_easy_copy.py')
