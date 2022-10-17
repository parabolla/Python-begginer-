# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе

class Number_class:
    def __init__(self, num_let=None):  # номер класса и буквы
        # self.number = number
        # self.letter = letter
        self.num_let = num_let  # наследовать

    # def num_let1(self):
    #     self.num_let = str(self.number) + self.letter


class Obj:
    def __init__(self, obj):  # наименование предметов
        self.obj = obj


class Teachers:
    def __init__(self, surname, obj="all", num_let):
        self.surname = surname
        self.obj = obj  # наследовать из Obj
        self.num_let = num_let  # наследовать из Number_class


# Должен быть как главный класс Родитель
class Students:
    def __init__(self, surname, teachers_name, parents, num_let, obj):
        self.surname = surname
        self.teachers_name = teachers_name
        self.parents = parents
        self.obj = obj
        self.num_let = num_let  # наследовать из Number_class
