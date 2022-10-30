# Enterprise
class People:
    def __init__(self, surname=str, name=str, birthday=str, telnum=int):

        self.__surname = surname
        self.__name = name
        self.__birthday = birthday
        self.__telnum = telnum  # телефонный номер

        @property
        def telnum(self):
            return self.__telnum

        @telnum.setter
        def telnum(self, value):
            if len(str(value)) < 11:
                print("Нужно ввести 11 значное число")
            else:
                return self.__telnum


class Employee(People):
    def __init__(self, surname, name, birthday, telnum, pernum=int, dpcode=int, salary=int):
        super().__init__(surname, name, birthday, telnum)
        self.__pernum = pernum  # id
        self.__dpcode = dpcode  # code
        self.__salary = salary  # оклад

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value

    @property
    def dpcode(self):
        return self.__dpcode

    @dpcode.setter
    def dpcode(self, value):
        return value

    @dpcode.deleter
    def dpcode(self):  # удаляем заводской код и оклад
        self.__dpcode = "уволен"
        self.__salary = "уволен"


emp1 = Employee("Petrov", "Petr", "24.3.2024", 89232432030, 1, 22133, 200)
# print(emp1.telnum, emp1.birthday)
# del emp1.dpcode
# print(emp1.salary)
# print(emp1.dpcode)
emp1.salary = 400  # меняем оклад
print(emp1.salary)
