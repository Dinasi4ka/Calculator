import math

def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def  multiplication(num1, num2):
    return num1 * num2

def  division(num1, num2):
    if num2 == 0:
        return "Ділення на нуль неможливе!"
    return num1 / num2

def  power(num1, num2):
    return pow(num1,num2)

def  square_root(num1):
    if num1 >= 0:
        return math.sqrt(num1)
    else:
        return "Неможливо обчислити квадратний корінь із від'ємного числа"

def  find_remainder(num1, num2):
    return num1 % num2