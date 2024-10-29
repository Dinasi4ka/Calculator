from termcolor import colored
from bll.classes.base_acii_art_generator import BaseAsciiArt

def get_user_input():
    return input("Введіть слово або фразу для ASCII-арту: ")

def get_available_fonts():
    art_generator = BaseAsciiArt()
    return art_generator.get_available_fonts()

def get_available_colors():
    art_generator = BaseAsciiArt()
    return art_generator.get_available_colors()


def preview_ascii_art(text, font, color, symbol, width_factor=1, height_factor=1):
    art_generator = BaseAsciiArt()
    ascii_art = art_generator.generate_art(text, font, symbol)
    scaled_art = art_generator.scale_ascii_art(ascii_art, width_factor, height_factor)
    colored_art = colored(scaled_art, color)
    
    print("\nПопередній перегляд ASCII-арту:\n")
    print(colored_art)
    return colored_art
