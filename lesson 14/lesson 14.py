import unittest


def prt(a, b):
    return a / b


assert prt(6, 6) == 1
assert prt(0, 6) == 1


class ASQ(unittest.TestCase):
    def test_qq(self):
        self.assertEqual(sum([1, 1]), 3)


if __name__ == "__main__":
    unittest.main()
