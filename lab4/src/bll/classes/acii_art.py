"""
Модуль для створення ASCII-арту з використанням бібліотеки pyfiglet і кольорового форматування termcolor.
"""

from src.bll.classes.base_acii_art_generator import BaseAsciiArt
import pyfiglet
from termcolor import colored

class AsciiArt(BaseAsciiArt):
    """
    Клас для генерації та виведення ASCII-арту з можливістю масштабування і вибору кольору.
    """

    def generate_art(self, text, symbol, width_factor, height_factor):
        """ Генерує ASCII-арт на основі введеного тексту і параметрів."""
        
        chosen_font = self.choose_font()  
        ascii_art = pyfiglet.figlet_format(text, font=chosen_font)
        ascii_art = ascii_art.replace("#", symbol).replace(".", symbol)
        return self.scale_ascii_art(ascii_art, width_factor, height_factor)

    def run(self):
        """
        Основний метод запуску генерації ASCII-арту.

        Користувач вводить параметри, після чого ASCII-арт генерується,
        форматується у вибраний колір і зберігається.
        """
        user_input, chosen_symbol, width_factor, height_factor = self.get_art_parameters()
        ascii_art = self.generate_art(user_input, chosen_symbol, width_factor, height_factor)

        chosen_color = self.choose_color()
        colored_art = colored(ascii_art, chosen_color)

        print("\nВаш ASCII-арт:\n")
        print(colored_art)
        self.save_art(colored_art)
