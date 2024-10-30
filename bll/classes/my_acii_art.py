from termcolor import colored
from bll.classes.base_acii_art_generator import BaseAsciiArt
from sources.ABC123dictionary import ABC123dictionary  

class MyAciiArt(BaseAsciiArt):
    def __init__(self):
        super().__init__()
        self.alphabet = ABC123dictionary  

    def generate_art(self, text, symbol, width_factor, height_factor, alignment='center'):
        art_lines = ['' for _ in range(5 * height_factor)]
        
        for char in text.upper():
            char_art = self.alphabet.get(char, self.alphabet[' '])
            for i, line in enumerate(char_art):
                art_lines[i] += line.replace('#', symbol) * width_factor
                art_lines[i] += ' ' * width_factor 

        console_width = 80
        
        if alignment == "center":
            aligned_art = [line.center(console_width) for line in art_lines]
        elif alignment == "right":
            aligned_art = [line.rjust(console_width) for line in art_lines]
        else: 
            aligned_art = [line.ljust(console_width) for line in art_lines]

        return '\n'.join(aligned_art)

    def choose_alignment(self):
        while True:
            alignment = input("Виберіть вирівнювання (left, center, right): ").strip().lower()
            if alignment in ["left", "center", "right"]:
                return alignment
            else:
                print("Недопустиме значення. Будь ласка, виберіть left, center або right.")

    def run(self):
        user_input, chosen_symbol, width_factor, height_factor = self.get_art_parameters()
        chosen_color = self.choose_color() 
        chosen_font = self.choose_font()
        alignment = self.choose_alignment()  

        ascii_art = self.generate_art(user_input, chosen_symbol, width_factor, height_factor, alignment)
        colored_art = colored(ascii_art, chosen_color)  
        print(colored_art)

        self.save_art(colored_art)
