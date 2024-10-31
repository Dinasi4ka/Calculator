import math

def addition(operand1, operand2):
    return operand1 + operand2

def subtraction(operand1, operand2):
    return operand1 - operand2

def  multiplication(operand1, operand2):
    return operand1 * operand2

def division(operand1, operand2):
    if operand2 == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе!")
    return operand1 / operand2

def  power(operand1, operand2):
    return pow(operand1,operand2)

def  square_root(operand1):
    if operand1 >= 0:
        return math.sqrt(operand1)
    else:
        return "Неможливо обчислити квадратний корінь із від'ємного числа"

def  find_remainder(operand1, operand2):
    return operand1 % operand2