import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bll.classes.api.menu import display_menu

def main():
    display_menu()

if __name__ == "__main__":
    main()
