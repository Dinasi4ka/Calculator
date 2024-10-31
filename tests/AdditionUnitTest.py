import random
import string
import unittest
from bll.classes.calculator.Calculator import Calculator

class CalculatorAdditionUnitTests(unittest.TestCase):

    def setUp(self):
        self.operator = "+"

    def test_add_positive_numbers(self):
        test_num1 = random.uniform(1, 100)
        test_num2 = random.uniform(1, 100)
        expected = test_num1 + test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertEqual(expected, result)

    def test_add_negative_numbers(self):
        test_num1 = random.uniform(-100, -1)
        test_num2 = random.uniform(-100, -1)
        expected = test_num1 + test_num2
        calc = Calculator()
        result = calc.calculate(test_num1, self.operator, test_num2)
        self.assertEqual(expected, result)

    def test_add_zero(self):
        test_num = random.uniform(-100, 100)
        expected = test_num
        calc = Calculator()
        result = calc.calculate(test_num, self.operator, 0)
        self.assertEqual(expected, result)

    def test_add_invalid_input(self):
        test_num1 = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        test_num2 = ''.join(random.choice(string.ascii_letters) for _ in range(10))
        calc = Calculator()
        with self.assertRaises(TypeError):
            calc.calculate(test_num1, self.operator, test_num2)

if __name__ == '__main__':
    unittest.main()
