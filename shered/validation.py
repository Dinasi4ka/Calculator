VALID_OPERATORS = ['+', '-', '*', '/', '^', '%', 'sq']

def validate_operator(operator):
    """
    Перевіряє, чи є оператор допустимим.
    """
    return operator in VALID_OPERATORS

def validate_number_input(input_str):
    """
    Перевіряє, чи введене значення є дійсним числом.
    Якщо неможливо перетворити на число, запитує повторно.
    """
    try:
        return float(input_str)
    except ValueError:
        print("Помилка: введіть дійсне число.")
        return validate_number_input(input("Введіть число: "))

def get_integer_input(prompt):
    """
    Запитує у користувача ціле число, поки не буде введено коректне значення.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Помилка: Будь ласка, введіть ціле число.")

def validate_text_input(user_input):
    """
    Перевіряє, чи введений текст складається лише з дозволених символів.
    """
    allowed_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 "
                              "АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯа бвгґдеєжзиіїйклмнопрстуфхцчшщьюя")
    for char in user_input:
        if char not in allowed_characters:
            raise ValueError("Введення містить недозволені символи.")
    return user_input

def validate_number_input(value, min_value=1):
    """
    Перевіряє, чи введене ціле число є більшим або рівним мінімальному значенню.
    """
    while True:
        try:
            num = int(value)
            if num < min_value:
                raise ValueError(f"Число має бути не менше {min_value}.")
            return num
        except ValueError:
            print("Введіть коректне ціле число.")
            value = input(f"Введіть число не менше {min_value}: ")

def validate_font_choice(font, allowed_fonts):
    """
    Перевіряє, чи вибраний шрифт є серед дозволених.
    """
    if font not in allowed_fonts:
        raise ValueError(f"Шрифт '{font}' не підтримується. Доступні шрифти: {', '.join(allowed_fonts)}")
    return font

def validate_color_choice(color, allowed_colors):
    """
    Перевіряє, чи вибраний колір є серед дозволених.
    """
    if color not in allowed_colors:
        raise ValueError(f"Колір '{color}' не підтримується. Доступні кольори: {', '.join(allowed_colors)}")
    return color

def validate_symbol(symbol):
    """
    Перевіряє, чи є символ допустимим.
    Якщо ні, використовує символ за замовчуванням.
    """
    allowed_symbols = ['#', '*', '@']
    if symbol in allowed_symbols:
        return symbol
    else:
        print(f"Недопустимий символ. Використано символ за замовчуванням: '#'.")
        return '#'
