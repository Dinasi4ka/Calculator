import subprocess

class LabFacade:
    """
    Клас LabFacade відповідає за запуск лабораторних робіт за номером.
    Він зберігає шляхи до скриптів лабораторних робіт та виконує їх.
    """
    def __init__(self):
        self.lab_map = {
            '1': r'c:\\Users\Admin\\Desktop\\Calculator\\lab1\\runner.py',
            '2': r'c:\\Users\Admin\\Desktop\\Calculator\\lab2\\runner.py',
            '3': r'c:\\Users\Admin\\Desktop\\Calculator\\lab3\\runner.py',
            '4': r'c:\\Users\Admin\\Desktop\\Calculator\\lab4\\runner.py',
            '5': r'c:\\Users\Admin\\Desktop\\Calculator\\lab5\\runner.py',
            '6': r'c:\\Users\Admin\\Desktop\\Calculator\\lab6\\runner.py',
            '7': r'c:\\Users\Admin\\Desktop\\Calculator\\lab7\\runner.py',
            '8': r'c:\\Users\Admin\\Desktop\\Calculator\\lab8\\runner.py',
        }

    def run_lab(self, lab_number):
        """
        Запускає лабораторну роботу за її номером.

        :param lab_number: Номер лабораторної роботи.
        """
        lab_path = self.lab_map.get(lab_number)
        if lab_path:
            subprocess.run(['python', lab_path])
        else:
            print("Невірний номер лабораторної роботи.")

def main():
    """
    Головна функція програми для вибору лабораторної роботи та її запуску.
    """
    facade = LabFacade()
    while True:
        print("\nВиберіть лабораторну роботу для запуску:")
        print("1. Лабораторна робота 1")
        print("2. Лабораторна робота 2")
        print("3. Лабораторна робота 3")
        print("4. Лабораторна робота 4")
        print("5. Лабораторна робота 5")
        print("6. Лабораторна робота 6")
        print("7. Лабораторна робота 7")
        print("8. Лабораторна робота 8")
        print("0. Вихід")

        choice = input("Ваш вибір: ")

        if choice == '0':
            print("Вихід з програми.")
            break
        facade.run_lab(choice)

if __name__ == "__main__":
    main()
