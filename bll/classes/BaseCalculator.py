from abc import ABC, abstractmethod
from dal.history import show_history, add_to_history

class BaseCalculator(ABC):
    def __init__(self):
        self.__decimal_places = 2  
        self.memory_value = None  

    @abstractmethod
    def calculate(self, operand1, operator, operand2=None):
        pass  

    def update_settings(self, decimal_places):
        self.__decimal_places = decimal_places
        print(f"Налаштування успішно змінено: {decimal_places} знаків після коми.")

    def display_result(self, result):
        print(f"Результат: {result:.{self.__decimal_places}f}")

    def run(self):
        while True:
            action = input("Виберіть дію: 1. Обчислити, 2. Змінити налаштування, 3. Вийти: ")
            if action == '1':
                operands = self.get_user_input()
                result = self.calculate(*operands)
                if result is not None:
                    self.display_result(result)
                    self.save_to_memory(result) 
            elif action == '2':
                self.change_settings()
            elif action == '3':
                if input("Вивести історію? (y/n): ").lower() == 'y':
                    self.show_history()
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")

    def get_user_input(self):
        use_memory = input("Використовувати число з пам'яті? (y/n): ").lower() == 'y'
        if use_memory:
            if self.memory_value is not None:
                print(f"Число з пам'яті: {self.memory_value}")
                operand1 = self.memory_value
            else:
                print("Немає збереженого значення в пам'яті.") 
                operand1 = float(input("Введіть перше число: "))
        else:
            operand1 = float(input("Введіть перше число: "))  

        operator = input("Введіть оператор (+, -, *, /, ^, sq, log, sin): ")
        operand2 = None
        if operator not in ['sq', 'log', 'sin']:
            operand2 = float(input("Введіть друге число: "))
        return operand1, operator, operand2

    def change_settings(self):
        new_decimal_places = int(input("Введіть кількість знаків після коми: "))
        self.update_settings(new_decimal_places)

    def save_to_memory(self, result):
        self.memory_value = round(result, self.__decimal_places)
        print(f"Збережено {self.memory_value} в пам'яті.")

    def show_history(self):
        show_history()
