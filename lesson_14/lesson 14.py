import unittest
from lesson_1.easy1 import calculation_sqrt
from lesson_6.hw06_normal import avg

class ASQ(unittest.TestCase):
    # Текст первого модуля
    def test_calculation_sqrt(self):
        self.assertEqual(calculation_sqrt(1, 4, 3), (-1.0, -3.0))
        self.assertEqual(calculation_sqrt(1, 8, 15), (-3.0, -5.0))
        self.assertEqual(calculation_sqrt(12, 7, 1), (-0.25, -0.3333333333333333))
        self.assertEqual(calculation_sqrt(0, 0, 0), ("нет корней"))
        self.assertEqual(calculation_sqrt(40, 50, 60), ("нет корней"))

    # Тест второго модуля
    def test_avg(self):
        self.assertEqual(avg(5, 10), (7.0710678118654755))
        self.assertEqual(avg(5, 5), (5))
        self.assertEqual(avg(12, 32), (19.595917942265423))
        self.assertEqual(avg(0, 0), (0.0))


if __name__ == "__main__":
    unittest.main()
