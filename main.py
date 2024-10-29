from ui.menu import display_menu, get_user_choice
from ui.menuBuilder import run_base_acii_art_generator, run_my_acii_art_generator, run_calculator

def main():
    print("\nЛаскаво просимо до генератора ASCII-арту та калькулятора!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            run_base_acii_art_generator()  
        elif choice == '2':
            run_my_acii_art_generator() 
        elif choice == '3':
            run_calculator()  
        elif choice == '4':
            print("До побачення!")
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
