import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))

from bll.classes.csv.data_repository import DataRepository
from menu import menu  

def main():
    repo = DataRepository('sources/seattle-weather.csv')
    data = repo.get_data()

    menu(data)

if __name__ == "__main__":
    main()

