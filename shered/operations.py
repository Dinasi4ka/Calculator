import math
from abc import ABC, abstractmethod
"""
Модуль для виконання арифметичних операцій
Цей модуль містить базові операції для калькулятора (додавання, віднімання, множення, ділення, піднесення до степеня, квадратний корінь та залишок від ділення).
"""
class Operation(ABC):
    """
    Абстрактний базовий клас для арифметичних операцій.
    """
    @abstractmethod
    def execute(self, operand1, operand2=None):
        """
        Виконує операцію з заданими операндами.
        """
        pass

class Addition(Operation):
    """
    Клас для операції додавання.
    """
    def execute(self, operand1, operand2):
        """
        Виконує додавання двох операндів.
        """
        return operand1 + operand2

class Subtraction(Operation):
    """
    Клас для операції віднімання.
    """
    def execute(self, operand1, operand2):
        """
        Виконує віднімання двох операндів.
        """
        return operand1 - operand2

class Multiplication(Operation):
    """
    Клас для операції множення.
    """
    def execute(self, operand1, operand2):
        """
        Виконує множення двох операндів.
        """
        return operand1 * operand2

class Division(Operation):
    """
    Клас для операції ділення.
    """
    def execute(self, operand1, operand2):
        """
        Виконує ділення двох операндів, підкидаючи помилку при діленні на нуль.
        """
        if operand2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        return operand1 / operand2

class Power(Operation):
    """
    Клас для операції піднесення до степеня.
    """
    def execute(self, operand1, operand2):
        """
        Виконує піднесення першого операнда до степеня другого операнда.
        """
        return pow(operand1, operand2)

class SquareRoot(Operation):
    """
    Клас для операції квадратного кореня.
    """
    def execute(self, operand1):
        """
        Виконує операцію квадратного кореня для одного операнда.
        Повертає повідомлення, якщо операнд від'ємний.
        """
        if operand1 >= 0:
            return math.sqrt(operand1)
        return "Неможливо обчислити квадратний корінь із від'ємного числа"

class FindRemainder(Operation):
    """
    Клас для операції знаходження залишку від ділення.
    """
    def execute(self, operand1, operand2):
        """
        Виконує операцію взяття залишку від ділення.
        """
        return operand1 % operand2
