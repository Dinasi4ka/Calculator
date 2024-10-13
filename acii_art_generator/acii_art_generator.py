import pyfiglet
from termcolor import colored

def save_to_file(ascii_art, filename="ascii_art.txt"):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(ascii_art)
    print(f"ASCII-арт збережено у файл: {filename}")

def scale_ascii_art(ascii_art, scale_factor):
    scaled_lines = []
    for line in ascii_art.splitlines():
        scaled_line = "".join(char * scale_factor for char in line)  
        for _ in range(scale_factor): 
            scaled_lines.append(scaled_line)
    return "\n".join(scaled_lines)

def generate_ascii_art(text, font="standard", color="white", symbol="#"):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    ascii_art = ascii_art.replace("#", symbol).replace(".", symbol) 
    colored_ascii_art = colored(ascii_art, color)
    return colored_ascii_art

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

def preview_ascii_art(text, font, color, symbol, scale_factor=1):
    ascii_art = generate_ascii_art(text, font, color, symbol)
    scaled_art = scale_ascii_art(ascii_art, scale_factor)
    print("\nПопередній перегляд ASCII-арту:\n")
    print(scaled_art)
    return scaled_art

def main():
    print("Ласкаво просимо до генератора ASCII-арту!")
    
    while True:  
        
        user_input = get_user_input()
        chosen_font = choose_font()
        chosen_color = choose_color()

        chosen_symbol = input("Введіть символ для ASCII-арту (за замовчуванням '#'): ") or "#"
        scale_factor = int(input("Введіть масштаб (ціле число, 1 для нормального розміру): ") or 1)

        ascii_art = preview_ascii_art(user_input, chosen_font, chosen_color, chosen_symbol, scale_factor)

        if input("Зберегти ASCII-арт? (y/n): ").lower() == 'y':
            filename = input("Введіть ім'я файлу для збереження (без розширення): ")
            save_to_file(ascii_art, f"{filename}.txt")

        if input("Бажаєте повторити? (y/n): ").lower() != 'y':
            break  

if __name__ == "__main__":
    main()


