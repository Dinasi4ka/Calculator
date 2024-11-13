import json
import csv
import re
from termcolor import colored
from tabulate import tabulate
from constants.globalVariables import history

def display_results(data):
    if isinstance(data, list):
        for item in data:
            print(colored(f"{item}", "green"))
    elif isinstance(data, dict):
        for key, value in data.items():
            print(colored(f"{key}: {value}", "yellow"))


def get_user_color_choice():
    colors = ["red", "green", "yellow", "blue", "magenta", "cyan", "white"]
    print("Available colors for headers:")
    for idx, color in enumerate(colors, 1):
        print(f"{idx}. {color}")
    
    choice = input("Choose a color for table headers by entering the number: ").strip()
    if choice.isdigit() and 1 <= int(choice) <= len(colors):
        return colors[int(choice) - 1]
    else:
        print("Invalid choice, defaulting to 'blue'.")
        return "blue"

def display_as_table(data, headers=None,header_color="blue"):
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
        print("No data to display in table format.")


def display_as_list(data):
    if data:
        for i, item in enumerate(data, start=1):
            if isinstance(item, dict):
                print(f"{i}. {str(item)}")
            else:
                print(f"{i}. {item}")
    else:
        print("No data to display in list format.")

def validate_date(date_str):
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_str))

def validate_phone(phone_str):
    pattern = r"^\+\d{1}-\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone_str))

def save_data(data, file_format):
    try:
        if file_format == 'json':
            with open('data.json', 'w') as f:
                json.dump(data, f, indent=4)
            print("Data saved to data.json")
        elif file_format == 'csv':
            with open('data.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
                    headers = data[0].keys()
                    writer.writerow(headers)  
                    for entry in data:
                        writer.writerow(entry.values())  
            print("Data saved to data.csv")
        elif file_format == 'txt':
            with open('data.txt', 'w') as f:
                for entry in data:
                    if isinstance(entry, dict):
                        for key, value in entry.items():
                            f.write(f"{key}: {value}\n")
                    else:
                        f.write(str(entry) + '\n')
            print("Data saved to data.txt")
        else:
            print("Invalid format. Please use json/csv/txt.")
    except Exception as e:
        print(f"Error saving data: {e}")


def log_request(action, endpoint, data, display_format, result):
    history.append({
        "Action": action,
        "Endpoint": endpoint,
        "Data": data,  
        "DisplayFormat": display_format,
        "Result": result 
    })
    print("Request logged to history.")


def show_history():
    if not history:
        print("No history available.")
    else:
        print("\nHistory of requests:")
        for i, entry in enumerate(history, 1):
            if isinstance(entry, dict):
                action = entry.get('Action', 'Unknown Action')
                endpoint = entry.get('Endpoint', 'Unknown Endpoint')
                data = entry.get('Data', 'No Data')
                display_format = entry.get('DisplayFormat', 'Unknown Format')
                print(f"{i}. Action: {action}, Endpoint: {endpoint}, Data: {data}, Display Format: {display_format}")
            else:
                print(f"{i}. {entry}")