from bll.classes.figures.Cube import Cube
from bll.classes.figures.Pyramid import Pyramid
from dal.filer import save_to_file
from bll.validation import validate_color_choice


class ThreeDArtGenerator:
    def __init__(self):
        self.art = None  
        self.color = 32  
        self.direction = True  

    def choose_shape(self):
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
        try:
            size = int(input("Введи новий розмір (не менше 3): "))
            if size < 3:
                print("Розмір має бути не менше 3.")
                return self.change_size()
            if self.art:
                self.art.size = size  
            else:
                print("Спочатку виберіть фігуру.")
        except ValueError:
            print("Неправильний вибір, спробуй ще раз")
            self.change_size()
        
    def get_available_colors(self):
        return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def choose_color(self):
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
        self.color = color_map[chosen_color]

    def change_color(self):
        color = int(input("Введіть код кольору (30-37): "))
        if 30 <= color <= 37:
            self.color = color
        else:
            print("Неправильний код кольору. Спробуйте ще раз.")
            self.change_color()
    
    def change_direction(self):
        self.direction = not self.direction
        print("Напрям успішно змінено")

    def get_art(self) -> str:
        color_text = '\033[%dm%s\033[0m'
        art = self.art.get_three_d_art()  
        colored_art = ""
        for line in art.split('\n'):
            colored_art += color_text % (self.color, line) + '\n'
        return colored_art

    def print_art(self):
        if self.art:
            print(self.get_art())
        else:
            print("Спочатку виберіть фігуру.")

    def save_art_into_file(self):
        if self.art:
            filename = input("Введіть ім'я файлу для збереження (без розширення): ") + ".txt"
            save_to_file(self.get_art(), filename)
        else:
            print("Спочатку виберіть фігуру.")

    def run(self):
        self.choose_shape()
        self.choose_color()
        self.print_art()
        save_choice = input("Бажаєте зберегти зображення у файл? (y/n): ").strip().lower()
        if save_choice == 'y':
            self.save_art_into_file()
        else:
            print("Зображення не буде збережено.")


