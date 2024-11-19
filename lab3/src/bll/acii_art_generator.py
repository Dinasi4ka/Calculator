import pyfiglet
from termcolor import colored

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
    return ['tty', 'banner', 'rozzo', 'standard', 'slant', 'big', 'doom', 'alligator', 'digital', 'cybermedium']

def get_available_colors():
    return ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']




