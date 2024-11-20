"""
Цей модуль містить функції для математичних операцій.
"""

import math

def addition(operand1, operand2):
    """
    Додає два числа.

    """
    return operand1 + operand2

def subtraction(operand1, operand2):
    """
    Віднімає два числа.

    """
    return operand1 - operand2

def  multiplication(operand1, operand2):
    """
    Множить два числа.

    """
    return operand1 * operand2

def  division(operand1, operand2):
    """
    Ділить два числа.

    """
    if operand2 == 0:
        return "Ділення на нуль неможливе!"
    return operand1 / operand2

def  power(operand1, operand2):
    """
    Підносить число до степеня

    """
    return pow(operand1,operand2)

def  square_root(operand1):
    """
    Знаходить корінь від числа

    """
    if operand1 >= 0:
        return math.sqrt(operand1)
    return "Неможливо обчислити квадратний корінь із від'ємного числа"

def  find_remainder(operand1, operand2):
    """
    Знаходить остачу від ділення

    """
    return operand1 % operand2

