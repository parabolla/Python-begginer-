# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    one = 1
    two = 1

    # print(one, two, end=' ')
    a = [one, two]
    for i in range(1, m + 1):
        one, two = two, one + two
        # a = print(two, end=" ")
        a.append(two)

    return a[n:m]


three = int(input("Введите m элемент :"))
print(fibonacci(1, three))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

1  #


def sort_to_max(origin_list):
    N = len(origin_list)  # число элементов в списке

    for i in range(1, N):
        for j in range(i, 0, -1):
            if origin_list[j] < origin_list[j - 1]:  # если число больше второго, меняем местами
                origin_list[j], origin_list[j - 1] = origin_list[j - 1], origin_list[j]
            else:
                break
        # print(origin_list)
    return origin_list


2  #
sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


def sort_to_max(origin_list):
    list_sort = 0
    list_help = 0
    list_two = []

    for i in origin_list:
        list_help = i
        for b in origin_list:
            if b >= i:
                list_sort = i
            elif b > list_help:
                break
            else:
                list_help = b
        list_two.append(list_help)
        origin_list.remove(list_help)
        list_help = 0

    # print(list_two)
    # print(origin_list)

    for i in origin_list:
        list_help = i
        for b in origin_list:
            if b >= i:
                list_sort = i
            elif b > list_help:
                break
            else:
                list_help = b
        list_two.append(list_help)
        origin_list.remove(list_help)
        list_help = 0

    for i in origin_list:
        list_help = i
        for b in origin_list:
            if b >= i:
                list_sort = i
            elif b > list_help:
                break
            else:
                list_help = b
        list_two.append(list_help)
        origin_list.remove(list_help)
        list_help = 0

    list_return = list_two + origin_list
    #
    # print(list_two)
    # print(origin_list)
    # print(list_return)
    return list_return


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_fil(fil):
    text = []
    numbers = []

    for i in fil:
        if isinstance(i, str):
            text.append(i)
        elif isinstance(i, int):
            numbers.append(i)
        else:
            print(i)

    return text, numbers


print(my_fil([1, "text", 3, 4, "text2", 6, "text3"]))

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
