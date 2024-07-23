import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calculator = Calculator()
        self.assertEqual(calculator.add(2, 3), 5)

    def test_subtract(self):
        calculator = Calculator()
        self.assertEqual(calculator.subtract(4, 1), 3)

    def test_multiply(self):
        calculator = Calculator()
        self.assertEqual(calculator.multiply(5, 6), 30)

    def test_divide(self):
        calculator = Calculator()
        self.assertEqual(calculator.divide(10, 2), 5)

    def test_divide_by_zero(self):
        calculator = Calculator()
        with self.assertRaises(ValueError):
            calculator.divide(10, 0)


if __name__ == '__main__':
    unittest.main()