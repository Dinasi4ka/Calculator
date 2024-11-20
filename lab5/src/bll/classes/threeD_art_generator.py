import sys
import os

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab5_root)


from src.bll.classes.figures.Cube import Cube
from src.bll.classes.figures.Pyramid import Pyramid
from shered.dal.filer import save_to_file
from shered.validation import validate_color_choice


class ThreeDArtGenerator:
    """
    Клас для генерації 3D-артів з вибором фігури та кольору.
    """

    def __init__(self):
        """
        Ініціалізація класу. Встановлення початкових значень для параметрів арт-генератора.
        """
        self.art = None 
        self.color = 32  
        self.direction = True 

    def choose_shape(self):
        """
        Вибір фігури для генерації 3D-арту.
        """
        shape = input("Виберіть фігуру (1 - Куб, 2 - Пірамід): ")
        size = int(input("Введіть розмір: "))
        
        if shape == '1':
            self.art = Cube(size)
        elif shape == '2':
            self.art = Pyramid(size)
        else:
            print("Невірний вибір. Спробуйте ще раз.")
            return self.choose_shape()

    def change_size(self):
        """
        Зміна розміру вибраної фігури.
        """
        try:
            size = int(input("Введіть новий розмір (не менше 3): "))
            if size < 3:
                print("Розмір має бути не менше 3.")
                return self.change_size()
            if self.art:
                self.art.size = size  
            else:
                print("Спочатку виберіть фігуру.")
        except ValueError:
            print("Неправильний вибір, спробуйте ще раз")
            self.change_size()
        
    def get_available_colors(self):
        """
        Отримання доступних кольорів для вибору.
        """
        return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def choose_color(self):
        """
        Вибір кольору для 3D-арту.
        """
        colors = self.get_available_colors()
        print("Доступні кольори:", colors)
        chosen_color = input("Виберіть колір з наведених: ").strip().lower()
        self.color = validate_color_choice(chosen_color, colors)
        color_map = {
            'red': 31,
            'green': 32,
            'yellow': 33,
            'blue': 34,
            'magenta': 35,
            'cyan': 36,
            'white': 37
        }
        self.color = color_map.get(chosen_color, 32)  

    def change_color(self):
        """
        Зміна кольору, введеного користувачем вручну.
        """
        color = int(input("Введіть код кольору (30-37): "))
        if 30 <= color <= 37:
            self.color = color
        else:
            print("Неправильний код кольору. Спробуйте ще раз.")
            self.change_color()

    def change_direction(self):
        """
        Зміна напрямку фігури.
        """
        self.direction = not self.direction
        print("Напрям успішно змінено.")

    def get_art(self) -> str:
        """
        Отримання 3D-арту у вигляді рядка з кольором.
        """
        color_text = '\033[%dm%s\033[0m' 
        art = self.art.get_three_d_art()  
        colored_art = ""
        for line in art.split('\n'):
            colored_art += color_text % (self.color, line) + '\n'
        return colored_art

    def print_art(self):
        """
        Виведення 3D-арту на екран.
        """
        if self.art:
            print(self.get_art())
        else:
            print("Спочатку виберіть фігуру.")

    def save_art_into_file(self):
        """
        Збереження 3D-арту у файл.
        """
        if self.art:
            filename = input("Введіть ім'я файлу для збереження (без розширення): ") + ".txt"
            save_to_file(self.get_art(), filename)
        else:
            print("Спочатку виберіть фігуру.")

    def run(self):
        """
        Запуск основного процесу генерації 3D-арту з вибором фігури, кольору, напрямку та збереження.
        """
        self.choose_shape()  
        self.choose_color() 
        self.print_art()  
        save_choice = input("Бажаєте зберегти зображення у файл? (y/n): ").strip().lower()
        if save_choice == 'y':
            self.save_art_into_file()  
        else:
            print("Зображення не буде збережено.")

