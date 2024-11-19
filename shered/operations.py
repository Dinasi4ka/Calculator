import math
from abc import ABC, abstractmethod

class Operation(ABC):
    @abstractmethod
    def execute(self, operand1, operand2=None):
        pass

class Addition(Operation):
    def execute(self, operand1, operand2):
        return operand1 + operand2

class Subtraction(Operation):
    def execute(self, operand1, operand2):
        return operand1 - operand2

class Multiplication(Operation):
    def execute(self, operand1, operand2):
        return operand1 * operand2

class Division(Operation):
    def execute(self, operand1, operand2):
        if operand2 == 0:
            raise ZeroDivisionError("Ділення на нуль неможливе!")
        return operand1 / operand2

class Power(Operation):
    def execute(self, operand1, operand2):
        return pow(operand1, operand2)

class SquareRoot(Operation):
    def execute(self, operand1):
        if operand1 >= 0:
            return math.sqrt(operand1)
        else:
            return "Неможливо обчислити квадратний корінь із від'ємного числа"

class FindRemainder(Operation):
    def execute(self, operand1, operand2):
        return operand1 % operand2