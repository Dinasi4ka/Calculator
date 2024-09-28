from functions.operations import addition, subtraction, division, multiplication, power, square_root, find_remainder
from functions.memory import save_result, get_result, has_memory
from functions.validation import validate_operator, validate_number_input
from functions.history import add_to_history, show_history, clear_history
from AppSettings import update_settings

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
                    num1 = get_result()
                    print(f"Число з пам'яті: {num1}")
                else:
                    print("Немає збереженого значення в пам'яті.")
                    continue
            else:
                num1 = validate_number_input(use_memory)

            operator = input("Введіть оператор (+, -, *, /, ^, %, sq): ").strip()
            while not validate_operator(operator):
                print("Невірний оператор. Спробуйте ще раз.")
                operator = input("Введіть оператор (+, -, *, /, ^, %, sq): ").strip()

            result = 0
            if operator == "sq":
                result = square_root(num1)
            else:
                num2 = validate_number_input(input("Введіть друге число: "))
                if operator == '+':
                    result = addition(num1, num2)
                elif operator == '-':
                    result = subtraction(num1, num2)
                elif operator == '*':
                    result = multiplication(num1, num2)
                elif operator == '/':
                    while True:
                        result = division(num1, num2)
                        if result == "Ділення на нуль неможливе!":
                            print(result)
                            num2 = validate_number_input(input("Введіть інше число для ділення: "))
                        else:
                            break
                elif operator == '^':
                    result = power(num1, num2)
                elif operator == '%':
                    result = find_remainder(num1, num2)

            if result is not None:
                result = round(result, decimal_places)
                print(f"Результат: {result}")
                save_result(result)
                add_to_history(num1, operator, num2, result)

        
            repeat = input("Хочете повторити обчислення? (y/n): ").lower()
            if repeat == 'n':
                if input("Показати історію обчислень? (y/n): ").lower() == 'y':
                    show_history()
                break
    
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
