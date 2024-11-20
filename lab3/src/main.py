import sys
import os

lab3_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab3_root)

from src.ui.art_interface import get_user_input, preview_ascii_art, choose_color, choose_font
from shered.dal.filer import save_to_file
from shered.validation import get_integer_input

def main():
    """
    Основна функція, що реалізує генератор ASCII-арту.
    Пропонує користувачеві вибір для створення ASCII-арту або виходу з програми.
    """
    print("Ласкаво просимо до генератора ASCII-арту!")

    while True:
        print("\nВиберіть опцію:")
        print("1 - Генератор ASCII-арту")
        print("2 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == '1':
            user_input = get_user_input()
            chosen_font = choose_font()
            chosen_color = choose_color()

            chosen_symbol = input("Введіть символ для ASCII-арту (за замовчуванням '#'): ") or "#"
            width_factor = get_integer_input("Введіть масштаб по ширині (ціле число, 1 для нормального розміру): ")
            height_factor = get_integer_input("Введіть масштаб по висоті (ціле число, 1 для нормального розміру): ")

            ascii_art = preview_ascii_art(user_input, chosen_font, chosen_color, chosen_symbol, width_factor, height_factor)

            if input("Зберегти ASCII-арт? (y/n): ").lower() == 'y':
                filename = input("Введіть ім'я файлу для збереження (без розширення): ")
                save_to_file(ascii_art, f"{filename}.txt")

        elif choice == '2':
            print("До побачення!")
            break

        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
