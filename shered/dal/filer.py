import os

def save_to_file(ascii_art, filename="ascii_art.txt"):
    try:
        if os.path.exists(filename):
            choice = input(f"Файл {filename} вже існує. Хочете його видалити? (y - очистити і перезаписати, n - зберегти під новим ім'ям): ").lower()
            if choice == 'y':
                os.remove(filename)
                print(f"Файл {filename} видалено.")
            elif choice == 'n':
                filename = input("Введіть нове ім'я файлу для збереження (без розширення): ") + ".txt"
                while os.path.exists(filename):
                    filename = input(f"Файл {filename} вже існує. Введіть інше ім'я: ") + ".txt"
        
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(ascii_art)
        print(f"ASCII-арт збережено у файл: {filename}")

    except OSError as e:
        print(f"Помилка при роботі з файлом: {e}")
