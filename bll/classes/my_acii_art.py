from termcolor import colored
from bll.classes.base_acii_art_generator import BaseAsciiArt
from sources.ABC123dictionary import ABC123dictionary  

class MyAciiArt(BaseAsciiArt):
    def __init__(self):
        super().__init__()
        self.alphabet = ABC123dictionary  

    def generate_art(self, text, symbol, width_factor, height_factor):
        art_lines = ['' for _ in range(5 * height_factor)]
        for char in text.upper():
            char_art = self.alphabet.get(char, self.alphabet[' '])
            for i, line in enumerate(char_art):
                art_lines[i] += line.replace('#', symbol) * width_factor
                art_lines[i] += ' ' * width_factor 

        return self.scale_ascii_art('\n'.join(art_lines), width_factor, height_factor)

    def align_text(self, art, alignment):
        max_length = max(len(line) for line in art.splitlines())
        aligned_art = []
        for line in art.splitlines():
            if alignment == 'left':
                aligned_art.append(line.ljust(max_length))
            elif alignment == 'center':
                aligned_art.append(line.center(max_length))
            elif alignment == 'right':
                aligned_art.append(line.rjust(max_length))
            else:
                aligned_art.append(line)  
        return '\n'.join(aligned_art)
    
    def choose_alignment(self):
        print("Виберіть вирівнювання (left, center, right):")
        alignment = input("Ваш вибір: ")
        return alignment if alignment in ['left', 'center', 'right'] else 'left'

    def run(self):
        user_input, chosen_symbol, width_factor, height_factor = self.get_art_parameters()
        chosen_color = self.choose_color() 
        chosen_font = self.choose_font()  
        alignment = self.choose_alignment()  

        ascii_art = self.generate_art(user_input, chosen_symbol, width_factor, height_factor)
        aligned_art = self.align_text(ascii_art, alignment)

        colored_art = colored(aligned_art, chosen_color)
        print(colored_art)

        self.save_art(colored_art)
