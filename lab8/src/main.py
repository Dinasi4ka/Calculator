import sys
import os

lab8_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.append(lab8_root)

from src.bll.classes.csv.data_repository import DataRepository
from src.ui.menu import menu  

def main():
    repo = DataRepository('sources/seattle-weather.csv')
    data = repo.get_data()

    menu(data)

if __name__ == "__main__":
    main()

