import random
import unittest
from bll.classes.calculator.Calculator import Calculator

class CalculatorSubtractionUnitTests(unittest.TestCase):
    
    def setUp(self):
        self.operator = "-"

    def test_subtract_positive_numbers(self):
        test_num1 = random.uniform(1, 100)
        test_num2 = random.uniform(1, 100)
        expected = test_num1 - test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertEqual(expected, result)

    def test_subtract_negative_numbers(self):
        test_num1 = random.uniform(-100, -1)
        test_num2 = random.uniform(-100, -1)
        expected = test_num1 - test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertEqual(expected, result)

    def test_subtract_zero(self):
        test_num = random.uniform(-100, 100)
        expected = test_num
        calc = Calculator()
        result = calc.calculate(test_num, self.operator, 0)
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()
