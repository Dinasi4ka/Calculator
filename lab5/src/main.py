import sys
import os

lab5_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab5_root)


from src.ui.menu import display_menu, get_user_choice
from src.ui.menuBuilder import run_three_d_art_generator

def main():
    print("\nЛаскаво просимо до генератора 3D ASCII-арту!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            run_three_d_art_generator()  
        elif choice == '2':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()