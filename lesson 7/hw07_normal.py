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

class School:
    def __init__(self, num_let=None, obj=None, name=None, surname=None):
        self.num_let = num_let  # наименование классов школы
        self.obj = obj  # предметы
        self.name = name
        self.surname = surname


class Teachers(School):
    def __init__(self, surname, obj, num_let):
        super(Teachers, self).__init__(surname)
        super(Teachers, self).__init__(obj)  # предметы
        super(Teachers, self).__init__(num_let)  # наименование классов школы


class Students(School):
    def __init__(self, name, surname, parent_m, parent_f, num_let):
        super(Students, self).__init__(name)
        super(Students, self).__init__(surname)
        self.parent_m = parent_m
        self.parent_f = parent_f
        super(Students, self).__init__(num_let)  # наименование классов школы


obj1 = School("math")
obj2 = School("rus_lang")

num_let1 = School("5V")
num_len2 = School("5K")

Teacher1 = Teachers("Ivanov", obj1, num_let1)
Teacher2 = Teachers("Petrov", [obj1, obj2], [num_let1, num_len2])

Pupil1 = Students("Max", "Sidorov", "Sidorova V.V.", "Sidorov M.P.", num_let1)
Pupil2 = Students("Alex", "Antonov", "Antonova D.D.", "Antonov S.Q.", num_let1)
