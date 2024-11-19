import sys
import os

lab7_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab7_root)

from src.ui.menu import display_menu, get_user_choice
from src.bll.classes.api.interaction import interact_with_user

def main():
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == '1':
            interact_with_user('get')
        elif choice == '2':
            interact_with_user('history')
        elif choice == '3':
            interact_with_user('save')
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()