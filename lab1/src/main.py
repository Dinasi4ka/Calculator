import sys
import os

lab1_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab1_root)

from src.functions.operations import addition, subtraction, division, multiplication, power, square_root, find_remainder
from shered.dal.memory import save_result, get_result, has_memory
from shered.validation import validate_operator, validate_number_input
from shered.dal.history import add_to_history, show_history, clear_history
from shered.AppSettings import update_settings

def main():
    
    change_settings = input("Хочете змінити налаштування калькулятора? (y/n): ").lower()
    if change_settings == 'y':
        settings = update_settings()
        decimal_places = settings["decimal_places"]
        print(f"Налаштування змінено: кількість десяткових розрядів - {decimal_places}")
    else:
        decimal_places = 2

    while True:
        try:
            use_memory = input("Введіть перше число (або M для значення з пам'яті): ").upper()
            if use_memory == 'M':
                if has_memory():
                    operand1 = get_result()
                    print(f"Число з пам'яті: {operand1}")
                else:
                    print("Немає збереженого значення в пам'яті.")
                    continue
            else:
                operand1 = validate_number_input(use_memory)

            operator = input("Введіть оператор (+, -, *, /, ^, %, sq): ").strip()
            while not validate_operator(operator):
                print("Невірний оператор. Спробуйте ще раз.")
                operator = input("Введіть оператор (+, -, *, /, ^, %, sq): ").strip()

            result = 0
            if operator == "sq":
                result = square_root(operand1)
            else:
                operand2 = validate_number_input(input("Введіть друге число: "))
                if operator == '+':
                    result = addition(operand1, operand2)
                elif operator == '-':
                    result = subtraction(operand1, operand2)
                elif operator == '*':
                    result = multiplication(operand1, operand2)
                elif operator == '/':
                    while True:
                        result = division(operand1, operand2)
                        if result == "Ділення на нуль неможливе!":
                            print(result)
                            operand2 = validate_number_input(input("Введіть інше число для ділення: "))
                        else:
                            break
                elif operator == '^':
                    result = power(operand1, operand2)
                elif operator == '%':
                    result = find_remainder(operand1, operand2)

            if result is not None:
                result = round(result, decimal_places)
                print(f"Результат: {result}")
                save_result(result, decimal_places)
                add_to_history(operand1, operator, operand2, result)

        
            repeat = input("Хочете повторити обчислення? (y/n): ").lower()
            if repeat == 'n':
                if input("Показати історію обчислень? (y/n): ").lower() == 'y':
                    show_history()
                break
    
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
