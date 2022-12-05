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
    def __init__(self, name, fname, salary=0, title="", hours=0, clock_rate=0):
        self.name = name
        self.fname = fname
        self.salary = int(salary)  # зарпалата
        self.title = title  # должность
        self.hours = int(hours)  # норма часов
        self.clock_rate = int(clock_rate)  # отработанно часов

    def get_salary(self):  # расчет зарплаты
        if self.hours > self.clock_rate:
            return [self.name, self.fname, self.clock_rate * (self.salary / self.hours)]
        elif self.clock_rate == self.hours:
            return [self.name, self.fname, self.salary]
        else:
            return [self.name, self.fname, abs(self.hours - self.clock_rate) * (
                    (self.salary / self.hours) * 2) + self.salary]


with open("hours_of", 'r') as hours:
    hours = [line.split() for line in hours][1:]
    workers_list = [Workers(first_name, last_name, hours=hours) for first_name, last_name, hours in hours]

with open("workers", 'r') as workers:
    workers = [line.split() for line in workers][1:]

    for name, fname, salary, title, clock_rate in workers:
        for worker in workers_list:
            if name == worker.name and fname == worker.fname:
                worker.salary = int(salary)
                worker.title = title
                worker.clock_rate = int(clock_rate)

with open("salaries_workers", "a") as sw:  # записываем в отдельный файл зарплаты
    for worker in workers_list:
        sw.write(str(worker.get_salary()))
        sw.write("\n")
