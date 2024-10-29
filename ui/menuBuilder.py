from bll.classes.Calculator import Calculator
from bll.classes.AdvancedCalculator import AdvancedCalculator
from bll.classes.acii_art import AsciiArt
from bll.classes.my_acii_art import MyAciiArt

def run_base_acii_art_generator():
    base_art = AsciiArt()
    base_art.run()  

def run_my_acii_art_generator():
    my_art = MyAciiArt()
    my_art.run()

def run_calculator():
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
