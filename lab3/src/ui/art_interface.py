from termcolor import colored
from src.bll.acii_art_generator import generate_ascii_art, scale_ascii_art, get_available_fonts, get_available_colors

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