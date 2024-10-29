from abc import ABC, abstractmethod

class BaseAsciiArt(ABC):  
    def __init__(self):
        pass  

    @abstractmethod
    def generate_art(self, text, symbol, width_factor, height_factor):
        pass

    @abstractmethod
    def run(self):
        pass

    def scale_ascii_art(self, ascii_art, width_factor, height_factor):
        scaled_lines = []
        for line in ascii_art.splitlines():
            scaled_line = "".join(char * width_factor for char in line)
            for _ in range(height_factor):
                scaled_lines.append(scaled_line)
        return "\n".join(scaled_lines)
    
    def choose_color(self):
        colors = self.get_available_colors()
        print("Доступні кольори:", colors)
        chosen_color = input("Виберіть колір з наведених: ")
        return chosen_color if chosen_color in colors else "white"
    
    def choose_font(self):
        fonts = self.get_available_fonts()
        print("Доступні шрифти:", fonts)
        chosen_font = input("Виберіть шрифт з наведених: ")
        return chosen_font if chosen_font in fonts else "standard"

    def get_available_fonts(self):
        return ['tty', 'banner', 'rozzo', 'standard', 'slant', 'big', 'doom', 'alligator', 'digital', 'cybermedium']

    def get_available_colors(self):
        return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

    def get_art_parameters(self):
        user_input = input("Введіть слово або фразу для ASCII-арту: ")
        chosen_symbol = input("Введіть символ для ASCII-арту (за замовчуванням '#'): ") or "#"
        width_factor = int(input("Введіть масштаб по ширині (ціле число, 1 для нормального розміру): "))
        height_factor = int(input("Введіть масштаб по висоті (ціле число, 1 для нормального розміру): "))
        return user_input, chosen_symbol, width_factor, height_factor

    def save_art(self, colored_art):
        if input("Зберегти ASCII-арт? (y/n): ").lower() == 'y':
            filename = input("Введіть ім'я файлу для збереження (без розширення): ")
            with open(f"{filename}.txt", "w") as file:
                file.write(colored_art)