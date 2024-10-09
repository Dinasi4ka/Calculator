from bll.classes.Calculator import Calculator
from bll.classes.AdvancedCalculator import AdvancedCalculator

def main():
    while True:
        calculator_type = input("Виберіть тип калькулятора (1 - Основний, 2 - Науковий): ")
        if calculator_type == '1':
            calculator = Calculator()
            break
        elif calculator_type == '2':
            calculator = AdvancedCalculator()
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")

    calculator.run()

if __name__ == "__main__":
    main()
