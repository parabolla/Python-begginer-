# Enterprise
import random
import random
from datetime import date


class People:
    def __init__(self, surname=str, name=str, birthday=str, telnum=int):

        self.surname = surname
        self.name = name
        self.birthday = birthday
        self.telnum = telnum  # телефонный номер
        if len(str(self.telnum)) == 11:
            self.telnum
        else:
            raise print("ошибка")


class Employee(People):
    def __init__(self, surname, name, birthday, telnum, pernum=int(0), dpcode=int(0), salary=int(0)):
        super().__init__(surname, name, birthday, telnum)
        self.__pernum = pernum  # id
        self.__dpcode = dpcode  # code
        self.__salary = salary  # оклад

    @property
    def pernum(self):
        return self.__pernum

    @property
    def dpcode(self):
        return self.__dpcode

    @property
    def salary(self):
        return self.__salary

    @salary.setter  # зп
    def salary(self, value):
        self.__salary = value

    @salary.setter  # автомазитизируем выдачу рандомных id
    def dpcode(self, value):
        self.__dpcode = value

    @salary.setter  # соединяем id и уникальный табельный номер
    def pernum(self, value):
        value += self.dpcode
        self.__pernum = value

    @dpcode.deleter
    def dpcode(self):  # удаляем заводской код и оклад
        self.__dpcode = "уволен"
        self.__salary = "уволен"


#
emp1 = Employee("Petrov",
                "Petr",
                2014 - 10 - 10,
                89232435123,
                1)
#
emp2 = Employee("Ivanov",
                "Ivan",
                2010 - 9 - 12,
                89232435522,
                2)

a = emp1.dpcode = 1
print(a)
b = emp1.pernum = 2
print(b)
# emp1.pernum(2)

# del emp1.dpcode
# print(emp1.pernum)
# print(emp2.pernum)
# print(emp1.dpcode)
# emp1.salary = 400  # меняем оклад
# print(emp1.salary)
