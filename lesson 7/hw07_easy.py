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
import math


class Trap:
    def __init__(self, one, two, three, four, p=0, s=0):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.p = p
        self.s = s

    def proverka_if(self):
        c = math.sqrt(((self.two - self.one) ** 2) + ((self.two - self.one) ** 2))
        d = math.sqrt(((self.four - self.three) ** 2) + ((self.four - self.three) ** 2))

        if c == d:
            print("Трапеция равнобокая")
        else:
            print("Трапеция неравнобокая")

    def side(self):
        c = math.sqrt(((self.two - self.one) ** 2) + ((self.two - self.one) ** 2))
        d = math.sqrt(((self.four - self.three) ** 2) + ((self.four - self.three) ** 2))
        a = math.sqrt(((self.three - self.two) ** 2) + ((self.three - self.two) ** 2))
        b = math.sqrt(((self.four - self.one) ** 2) + ((self.four - self.one) ** 2))
        print("Длина сторон: " + "\nAB: ", a, "\nBC: ", c, "\nCD: ", d, "\nDC: ", b)

    def perimeter(self):
        c = math.sqrt(((self.two - self.one) ** 2) + ((self.two - self.one) ** 2))
        d = math.sqrt(((self.four - self.three) ** 2) + ((self.four - self.three) ** 2))
        a = math.sqrt(((self.three - self.two) ** 2) + ((self.three - self.two) ** 2))
        b = math.sqrt(((self.four - self.one) ** 2) + ((self.four - self.one) ** 2))
        return a + b + c + d
        print("Периметр:", P)

    def area(self):
        c = math.sqrt(((self.two - self.one) ** 2) + ((self.two - self.one) ** 2))
        d = math.sqrt(((self.four - self.three) ** 2) + ((self.four - self.three) ** 2))
        a = math.sqrt(((self.three - self.two) ** 2) + ((self.three - self.two) ** 2))
        b = math.sqrt(((self.four - self.one) ** 2) + ((self.four - self.one) ** 2))
        return ((a + b) / 2) * (math.sqrt((c ** 2) - ((((b - a) ** 2) + (c ** 2) - (d ** 2)) / (2 * (b - a)))))
        print("Площадь:", S, "\n")


trap1 = Trap(5, 7, 2, 2)
trap1.proverka_if()
trap1.side()
print("Периметр: ", trap1.perimeter())
print("Площадь: ", trap1.area())
