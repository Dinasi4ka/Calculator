from bll.classes.calculator.BaseCalculator import BaseCalculator
from bll.operations import addition, subtraction, division, multiplication, power, square_root
from dal.memory import save_result, get_result, has_memory
from dal.history import add_to_history, show_history

class Calculator(BaseCalculator):
    def __init__(self, operand1=None, operand2=None, operator=None):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.result = None

    def calculate(self, operand1, operator, operand2=None):

        if not isinstance(operand1, (int, float)) or (operand2 is not None and not isinstance(operand2, (int, float))):
            raise TypeError("Операнди повинні бути числами.")
        
        if operator == '+':
            result = addition(operand1, operand2)
        elif operator == '-':
            result = subtraction(operand1, operand2)
        elif operator == '*':
            result = multiplication(operand1, operand2)
        elif operator == '/':
            result = division(operand1, operand2)
        elif operator == '^':
            result = power(operand1, operand2)
        elif operator == 'sq':
            result = square_root(operand1)
        elif operator in ['log', 'sin']: 
            print(f"Помилка: Оператор '{operator}' недоступний у звичайному калькуляторі.")
            return None
        else:
            raise ValueError("Невідомий оператор")
        
        add_to_history(operand1, operator, operand2, result)
        return result

    def run(self):
        super().run()