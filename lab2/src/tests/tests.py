import unittest
import os
import sys

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab2_root)
main_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
sys.path.append(main_root)

from src.bll.classes.Calculator import Calculator

class TestCalculator(unittest.TestCase):
    """
    Клас для тестування методів калькулятора.
    """

    def setUp(self):
        """
        Налаштовуємо початковий стан для кожного тесту.
        """
        self.calculator = Calculator()

    def test_add(self):
        """
        Тестуємо додавання.
        """
        self.assertEqual(self.calculator.calculate(5, "+", 3), 8)
        self.assertEqual(self.calculator.calculate(-2, "+", -3), -5)
        self.assertEqual(self.calculator.calculate(0, "+", 0), 0)

    def test_subtract(self):
        """
        Тестуємо віднімання.
        """
        self.assertEqual(self.calculator.calculate(10, "-", 5), 5)
        self.assertEqual(self.calculator.calculate(-5, "-", -3), -2)
        self.assertEqual(self.calculator.calculate(5, "-", 10), -5)

    def test_multiply(self):
        """
        Тестуємо множення.
        """
        self.assertEqual(self.calculator.calculate(4, "*", 3), 12)
        self.assertEqual(self.calculator.calculate(-2, "*", 3), -6)
        self.assertEqual(self.calculator.calculate(0, "*", 5), 0)

    def test_divide(self):
        """
        Тестуємо ділення.
        """
        self.assertEqual(self.calculator.calculate(10, "/", 2), 5)
        self.assertEqual(self.calculator.calculate(-6, "/", 3), -2)
        self.assertAlmostEqual(
            self.calculator.calculate(1, "/", 3), 0.333333, places=5
        )

        with self.assertRaises(ZeroDivisionError):
            self.calculator.calculate(10, "/", 0)

if __name__ == "__main__":
    unittest.main()

