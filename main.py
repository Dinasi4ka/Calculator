from bll.classes.Calculator import Calculator
from bll.classes.AdvancedCalculator import AdvancedCalculator
from ui.art_interface import get_user_input, preview_ascii_art, choose_color, choose_font
from dal.filer import save_to_file


def main():
    print("Ласкаво просимо до генератора ASCII-арту та калькулятора!")
    
    while True:
        print("\nВиберіть опцію:")
        print("1 - Генератор ASCII-арту")
        print("2 - Запустити калькулятор")
        print("3 - Вихід")

        choice = input("Ваш вибір: ")
        
        if choice == '1':
            user_input = get_user_input()
            chosen_font = choose_font()
            chosen_color = choose_color()

            chosen_symbol = input("Введіть символ для ASCII-арту (за замовчуванням '#'): ") or "#"
            width_factor = int(input("Введіть масштаб по ширині (ціле число, 1 для нормального розміру): ") or 1)
            height_factor = int(input("Введіть масштаб по висоті (ціле число, 1 для нормального розміру): ") or 1)

            ascii_art = preview_ascii_art(user_input, chosen_font, chosen_color, chosen_symbol, width_factor, height_factor)

            if input("Зберегти ASCII-арт? (y/n): ").lower() == 'y':
                filename = input("Введіть ім'я файлу для збереження (без розширення): ")
                save_to_file(ascii_art, f"{filename}.txt")

        elif choice == '2':
            while True:
                calculator_type = input("Виберіть тип калькулятора (1 - Основний, 2 - Науковий): ")
                if calculator_type == '1':
                    calculator = Calculator()
                    print("Вибрано основний калькулятор.")
                    break
                elif calculator_type == '2':
                    calculator = AdvancedCalculator()
                    print("Вибрано науковий калькулятор.")
                    break
                else:
                    print("Невірний вибір. Спробуйте ще раз.")
            calculator.run()

        elif choice == '3':
            print("До побачення!")
            break
        
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()