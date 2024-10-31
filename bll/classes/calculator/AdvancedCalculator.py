import math
from bll.classes.calculator.BaseCalculator import BaseCalculator

class AdvancedCalculator(BaseCalculator):
    def __init__(self):
        super().__init__()

    def calculate(self, operand1, operator, operand2=None):
        if operator == 'log':
            if operand1 <= 0:
                print("Логарифм може бути обчислений лише для додатних чисел.")
                return None  
            return math.log(operand1)
        elif operator == 'sin':
            return math.sin(math.radians(operand1))
        else:
            return super().calculate(operand1, operator, operand2)

    def run(self):
        print("Запущено розширений калькулятор")  
        super().run()
