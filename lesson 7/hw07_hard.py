# Задание-1: Решите задачу (дублированную ниже):

# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки они получают
# удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

# С использованием классов.
# Реализуйте классы сотрудников так, чтобы на вход функции-конструктора
# каждый работник получал строку из файла

class Workers:
    def __init__(self, name, fname, salary, title, hours, clock_rate):
        self.name = name
        self.fname = fname
        self.salary = salary  # зарпалата
        self.title = title  # должность
        self.hours = hours  # норма часов
        self.clock_rate = clock_rate  # отработанно часов

    def get_salary(self):  # расчет зарплаты
        if self.hours > self.clock_rate:
            return self.name, self.fname, self.clock_rate * (self.salary / self.hours)
        elif self.clock_rate == self.hours:
            return self.name, self.fname, self.salary
        else:
            return self.name, self.fname, abs(self.hours - self.clock_rate) * (
                    (self.salary / self.hours) * 2) + self.salary


worker1 = Workers("Петр", "Алексеев", 22000, "Прораб", 140, 140)
a = worker1.get_salary()
print(a)
