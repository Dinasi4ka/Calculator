import sys
import os

lab4_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "lab4", "src"))
sys.path.append(lab4_root)

from src.ui.menu import display_menu, get_user_choice
from src.ui.menuBuilder import run_base_acii_art_generator, run_my_acii_art_generator

def main():
    """
    Основна функція, що реалізує генератор ASCII-арту з вибором користувача.
    Користувач може вибрати один з варіантів:
    1 - Базовий генератор ASCII-арту
    2 - Мій генератор ASCII-арту
    3 - Вихід з програми
    """
    print("\nЛаскаво просимо до генератора ASCII-арту!")
    
    while True:
        choice = get_user_choice()  
        
        if choice == '1':
            run_base_acii_art_generator()  
        elif choice == '2':
            run_my_acii_art_generator()  
        elif choice == '3':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
