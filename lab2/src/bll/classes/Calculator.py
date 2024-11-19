import sys
import os

lab2_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab2_root)


from src.bll.classes.BaseCalculator import BaseCalculator
from shered.operations import Addition, Subtraction, Division, Multiplication, Power, SquareRoot, FindRemainder
from shered.dal.memory import save_result, get_result, has_memory
from shered.dal.history import add_to_history, show_history

class Calculator(BaseCalculator):
    def __init__(self, operand1=None, operand2=None, operator=None):
        super().__init__()
        self.operand1 = operand1
        self.operand2 = operand2
        self.operator = operator
        self.result = None

    def get_operation(self, operator):
        if operator == '+':
            return Addition()
        elif operator == '-':
            return Subtraction()
        elif operator == '*':
            return Multiplication()
        elif operator == '/':
            return Division()
        elif operator == '^':
            return Power()
        elif operator == 'sq':
            return SquareRoot()
        elif operator == '%':
            return FindRemainder()
        else:
            raise ValueError("Невідома операція")

    def calculate(self, operand1, operator, operand2=None):
        if not isinstance(operand1, (int, float)) or (operand2 is not None and not isinstance(operand2, (int, float))):
            raise TypeError("Операнди повинні бути числами.")

        try:
            operation = self.get_operation(operator)
        except ValueError as e:
            print(e)
            return None

        result = operation.execute(operand1, operand2)

        if result is None:
            print(f"Помилка: Оператор '{operator}' не підтримується.")
            return None

        add_to_history(operand1, operator, operand2, result)
        return result

    def run(self):
        super().run()
