__author__ = 'Ткачев И.П.'

# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"

age = int(input("Укажите свой возраст "))
if age >= 18:
    print("доступ разрешен")
else:
    print("Извините, пользоваться данным ресурсом можно только с 18 лет")

# # Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# # используя цикл с предусловием while или for in
# # вывести в одну строку через пробел соотвествующие числа от 0 до 20
# # Пример работы:
# # $ "Четные или нечетные?"
# # четные
# # 0 2 4 6 8 10 12 14 16 18 20
# # $ "Четные или нечетные?"
# # нечетные
# # 1 3 5 7 9 11 13 15 17 19
# # $ "Четные или нечетные?"
# # qwerty (или любая другая строка)
# # Я не понимаю, что вы от меня хотите...
#
cht = str(input("Чет или нечет?"))
if cht == "чет":
    for i in range(0, 22, 2):  # делаем перебор с каждого второго знака после 0
        print(i, end=" ")
elif cht == "нечет":
    for i in range(1, 20, 2):  # делаем перебор с каждого второго знака после 1
        print(i, end=" ")
else:
    print("Я не понимаю, что вы от меня хотите...")

# Задача-3: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Выполнение через While
one = int(input("Введите натуральные числа : "))
# x = one  # неразбериха с int и str
a = len(str(one))  # вычисляем кол. знаков для кол. итераций
b = len(str(one))  # # вычисляем кол. знаков для умножения в степень
c = 1  # итерации
str = 0  # переменная для хранения/сравнения значений
while c != a + 1:  # выполняем, пока количесво строк не сравняется с кол. итераций
    cal = (one // (10 ** (b - 1)) % 10)  # высчитываем первый знак
    if str >= cal:  # если переменная >= высчитываемой цифры, пропускаем присваение ее к новому значению
        c += 1
        b -= 1
        continue
    else:
        c += 1  # увеличиваем итерацию
        b -= 1  # снижаем с каждой итерацией степень
        str = cal  # присваение переменной высчитываемого знака

print("Самая большая цифра ", str)

# Выполнение через for
per = int(input())
# x = per
z = len(str(per))  # подсчитываем кол. символов для range
one = 0
two = 0
for i in range(z):  # проходим z раз.
    one = (per // (10 ** (i + 1 - 1)) % 10)  # проходим по каждой цифре и сравниваем ее с предыдущей
    if one > two:  # если первое значение больше второго, оно берется за сравниваемое
        two = one
    else:
        continue
print("Самая большая цифра ", two)
