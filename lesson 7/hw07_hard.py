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
    new_list2 = [line.split() for line in hours]

with open("workers", 'r') as workers:
    for new_list in workers.readlines():
        try:
            workers = Workers(*new_list.split())
        except IndexError:
            continue
            print("Невереные данные в строке: {}".format(new_list))
        except ValueError:
            continue
            print("Проверьте данные в строке: {}".format(new_list))

with open("salaries_workers", "a") as sw:  # записываем в отдельный файл зарплаты
    sw.write(str(workers.get_salary()))
    sw.write("\n")
