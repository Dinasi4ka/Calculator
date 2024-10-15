import pyfiglet
from termcolor import colored

def save_to_file(ascii_art, filename="ascii_art.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл: {filename}")

def scale_ascii_art(ascii_art, width_factor, height_factor):
    scaled_lines = []
    for line in ascii_art.splitlines():
        scaled_line = "".join(char * width_factor for char in line)
        for _ in range(height_factor):
            scaled_lines.append(scaled_line)
    return "\n".join(scaled_lines)

def generate_ascii_art(text, font="standard", symbol="#"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    ascii_art = ascii_art.replace("#", symbol).replace(".", symbol)
    return ascii_art

def get_available_fonts():
    return pyfiglet.FigletFont.getFonts()

def get_available_colors():
    return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def get_user_input():
    return input("Введіть слово або фразу для ASCII-арту: ")

def choose_font():
    fonts = get_available_fonts()
    print("Доступні шрифти:", fonts)
    chosen_font = input("Виберіть шрифт з наведених: ")
    return chosen_font if chosen_font in fonts else "standard"

def choose_color():
    colors = get_available_colors()
    print("Доступні кольори:", colors)
    chosen_color = input("Виберіть колір з наведених: ")
    return chosen_color if chosen_color in colors else "white"

def preview_ascii_art(text, font, color, symbol, width_factor=1, height_factor=1):
    ascii_art = generate_ascii_art(text, font, symbol)
    scaled_art = scale_ascii_art(ascii_art, width_factor, height_factor)
    colored_art = colored(scaled_art, color)
    
    print("\nПопередній перегляд ASCII-арту:\n")
    print(colored_art)
    return colored_art

def main():
    print("Ласкаво просимо до генератора ASCII-арту!")
    
    while True:  
        
        user_input = get_user_input()
        chosen_font = choose_font()
        chosen_color = choose_color()

        chosen_symbol = input("Введіть символ для ASCII-арту (за замовчуванням '#'): ") or "#"
        width_factor = int(input("Введіть масштаб по ширині (ціле число, 1 для нормального розміру): ") or 1)
        height_factor = int(input("Введіть масштаб по висоті (ціле число, 1 для нормального розміру): ") or 1)

        ascii_art = preview_ascii_art(user_input, chosen_font, chosen_color, chosen_symbol, width_factor, height_factor)

        if input("Зберегти ASCII-арт? (y/n): ").lower() == 'y':
            filename = input("Введіть ім'я файлу для збереження (без розширення): ")
            save_to_file(ascii_art, f"{filename}.txt")

        if input("Бажаєте повторити? (y/n): ").lower() != 'y':
            break  

if __name__ == "__main__":
    main()
