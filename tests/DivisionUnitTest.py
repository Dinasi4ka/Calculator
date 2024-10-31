import random
import unittest
from bll.classes.calculator.Calculator import Calculator

class CalculatorDivisionUnitTests(unittest.TestCase):
    
    def setUp(self):
        self.operator = "/"

    def test_divide_positive_numbers(self):
        test_num1 = random.uniform(1, 100)
        test_num2 = random.uniform(1, 100)
        expected = test_num1 / test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertAlmostEqual(expected, result)

    def test_divide_by_zero(self):
        test_num = random.uniform(1, 100)
        calc = Calculator()
        with self.assertRaises(ZeroDivisionError):
            calc.calculate(test_num, self.operator, 0)

if __name__ == '__main__':
    unittest.main()
