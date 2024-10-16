
VALID_OPERATORS = ['+', '-', '*', '/', '^', '%', 'sq']

def validate_operator(operator):
    return operator in VALID_OPERATORS

def validate_number_input(input_str):
    try:
        return float(input_str)
    except ValueError:
        print("Помилка: введіть дійсне число.")
        return validate_number_input(input("Введіть число: "))
    
def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Помилка: Будь ласка, введіть ціле число.")
