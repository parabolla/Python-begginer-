# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

class Threeangle:
    def __init__(self, one=0, two=0, three=0):
        self.one = one
        self.two = two
        self.three = three

    def calculation_s(self):  # площадь
        return self.one * self.two * 0.5

    def calculation_h(self):  # высота
        return (self.one + self.two + self.three) / 2

    def calculation_p(self):  # периметр
        return self.one + self.two + self.three


t1 = Threeangle(10, 20, 3)
print(t1.calculation_s())
print(t1.calculation_h())
print(t1.calculation_p())

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
