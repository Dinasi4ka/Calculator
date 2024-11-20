import json
import csv
import re
from termcolor import colored
from tabulate import tabulate
from shered.constants.globalVariables import history


def display_results(data):
    """
    Виводить результати у форматі списку або словника з кольоровим виведенням.
    """
    if isinstance(data, list):
        for item in data:
            print(colored(f"{item}", "green"))
    elif isinstance(data, dict):
        for key, value in data.items():
            print(colored(f"{key}: {value}", "yellow"))


def get_user_color_choice():
    """
    Запитує користувача вибір кольору для заголовків таблиці та повертає обраний колір.
    """
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print("Доступні кольори для заголовків:")
    for idx, color in enumerate(colors, 1):
        print(f"{idx}. {color}")

    choice = input("Оберіть колір для заголовків таблиці, ввівши номер: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(colors):
        return colors[int(choice) - 1]
    else:
        print("Невірний вибір, за замовчуванням обрано 'blue'.")
        return "blue"


def display_as_table(data, headers=None, header_color="blue"):
    """
    Виводить дані у форматі таблиці з можливими налаштуваннями для заголовків та кольору заголовків.
    """
    if data and isinstance(data, list) and all(isinstance(item, dict) for item in data):
        if not headers:
            all_keys = set().union(*(item.keys() for item in data))
            headers = list(all_keys)[:6]

        header_color = get_user_color_choice()

        filtered_data = [
            {key: item.get(key, '') for key in headers} for item in data
        ]

        rows = [list(item.values()) for item in filtered_data]
        colored_headers = [colored(header, header_color) for header in headers]

        print(tabulate(rows, headers=colored_headers, tablefmt='pretty'))
    else:
        print("Немає даних для відображення у форматі таблиці.")


def display_as_list(data):
    """
    Виводить дані у форматі нумерованого списку.
    """
    if data:
        for i, item in enumerate(data, start=1):
            if isinstance(item, dict):
                print(f"{i}. {str(item)}")
            else:
                print(f"{i}. {item}")
    else:
        print("Немає даних для відображення у форматі списку.")


def validate_date(date_str):
    """
    Перевіряє, чи відповідає надана строка дати формату YYYY-MM-DD.
    """
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))


def validate_phone(phone_str):
    """
    Перевіряє, чи відповідає надана строка телефону формату +X-XXX-XXX-XXXX.
    """
    pattern = r"^\+\d{1}-\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone_str))


def save_data(data, file_format):
    """
    Зберігає дані у зазначеному форматі (json, csv або txt).
    """
    try:
        if file_format == 'json':
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Дані збережено у data.json")
        elif file_format == 'csv':
            with open('data.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    headers = data[0].keys()
                    writer.writerow(headers)
                    for entry in data:
                        writer.writerow(entry.values())
            print("Дані збережено у data.csv")
        elif file_format == 'txt':
            with open('data.txt', 'w') as f:
                for entry in data:
                    if isinstance(entry, dict):
                        for key, value in entry.items():
                            f.write(f"{key}: {value}\n")
                    else:
                        f.write(str(entry) + '\n')
            print("Дані збережено у data.txt")
        else:
            print("Невірний формат. Використовуйте json/csv/txt.")
    except Exception as e:
        print(f"Помилка при збереженні даних: {e}")


def log_request(action, endpoint, data, display_format, result):
    """
    Логування запиту з зазначеними дією, кінцевою точкою, даними, форматом відображення та результатом.
    """
    history.append({
        "Action": action,
        "Endpoint": endpoint,
        "Data": data,
        "DisplayFormat": display_format,
        "Result": result
    })
    print("Запит зафіксовано в історії.")


def show_history():
    """
    Виводить історію всіх зафіксованих запитів.
    """
    if not history:
        print("Історія відсутня.")
    else:
        print("\nІсторія запитів:")
        for i, entry in enumerate(history, 1):
            if isinstance(entry, dict):
                action = entry.get('Action', 'Невідома дія')
                endpoint = entry.get('Endpoint', 'Невідома точка')
                data = entry.get('Data', 'Немає даних')
                display_format = entry.get('DisplayFormat', 'Невідомий формат')
                print(f"{i}. Дія: {action}, Точка: {endpoint}, Дані: {data}, Формат відображення: {display_format}")
            else:
                print(f"{i}. {entry}")
