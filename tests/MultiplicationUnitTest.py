import random
import unittest
from bll.classes.calculator.Calculator import Calculator

class CalculatorMultiplicationUnitTests(unittest.TestCase):
    
    def setUp(self):
        self.operator = "*"

    def test_multiply_positive_numbers(self):
        test_num1 = random.uniform(1, 100)
        test_num2 = random.uniform(1, 100)
        expected = test_num1 * test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertEqual(expected, result)

    def test_multiply_by_zero(self):
        test_num = random.uniform(1, 100)
        calc = Calculator()
        result = calc.calculate(test_num, self.operator, 0)
        self.assertEqual(0, result)

if __name__ == '__main__':
    unittest.main()
