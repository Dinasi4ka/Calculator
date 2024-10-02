import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from functions.operations import addition, subtraction, division, multiplication, power, square_root, find_remainder
from functions.memory import save_result, get_result, has_memory
from functions.validation import validate_operator, validate_number_input
from functions.history import add_to_history, show_history, clear_history
from AppSettings import update_settings


class Calculator:

    def __init__(self):
        self.decimal_places = 2
        self.history = []
    
    def update_settings(self):
        if input("Хочете змінити налаштування калькулятора? (y/n): ").lower() == 'y':
            self.decimal_places = update_settings()["decimal_places"]
            print(f"Налаштування змінено: кількість десяткових розрядів - {self.decimal_places}")
    
    def user_input(self):
        use_memory = input("Введіть перше число (або M для значення з пам'яті): ").upper()
        if use_memory == 'M':
            if has_memory():
                operand1 = get_result()
                print(f"Число з пам'яті: {operand1}")
                return operand1
            else:
                print("Немає збереженого значення в пам'яті.")
                return None
        else:
            return validate_number_input(use_memory)
        
    def validate_operator_input(self):
        operator = input("Введіть оператор (+, -, *, /, ^, %, sq): ").strip()
        while not validate_operator(operator):
            operator = input("Невірний оператор. Спробуйте ще раз: ").strip()
        return operator
    
    def calculate(self, operand1, operator, operand2 = None):
        if operator == "sq":
            return square_root(operand1)
        else:
            if operator == '+':
                return addition(operand1, operand2)
            elif operator == '-':
                return subtraction(operand1, operand2)
            elif operator == '*':
                return multiplication(operand1, operand2)
            elif operator == '/':
                return self.handle_division(operand1, operand2)
            elif operator == '^':
                return power(operand1, operand2)
            elif operator == '%':
                return find_remainder(operand1, operand2)
            
    def handle_division(self, operand1, operand2):
        while True:
            result = division(operand1, operand2)
            if result == "Ділення на нуль неможливе!":
                print(result)
                operand2 = validate_number_input(input("Введіть інше число для ділення: "))
            else:
                return result
    
    def display_result(self, result):
        print(f"Результат: {result:.{self.decimal_places}f}")

    def run(self):
        self.update_settings()  
        while True:
            try:
                operand1 = self.user_input()
                if operand1 is None:
                    continue  
            
                operator = self.validate_operator_input()
                operand2 = None
                if operator != "sq":  
                    operand2 = validate_number_input(input("Введіть друге число: "))

                result = self.calculate(operand1, operator, operand2)
                self.display_result(result)

                save_result(result, self.decimal_places)
                add_to_history(operand1, operator, operand2, result)
            
                if not self.repeat_calculation():  
                    break

            except ValueError as e:
                print(f"Error: {e}")
    
    def repeat_calculation(self):
        while True:
            repeat = input("Хочете повторити обчислення? (y/n): ").lower()
            if repeat == 'n':
                if input("Показати історію обчислень? (y/n): ").lower() == 'y':
                    show_history()
                print("Дякуємо за користування калькулятором!")
                return False  
            elif repeat == 'y':
                return True  
            else:
                print("Невірна команда. Спробуйте ще раз.")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run()
    sys.exit()






























