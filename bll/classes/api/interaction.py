from bll.classes.api.ApiHandler import APIHandler
from bll.classes.api.user_repository import UserRepository
from bll.classes.api.display import DisplayStrategy, DisplayFactory
from constants.globalVariables import history
from utils import display_results, display_as_table, display_as_list, validate_date, validate_phone, show_history, save_data, log_request

def get_user_input():
    action = input("Choose view format: 1. Table 2. List: ").strip()
    if action == '1':
        return 'table'
    elif action == '2':
        return 'list'
    else:
        print("Invalid input. Please try again.")
        return get_user_input()

def interact_with_user(action):
    api = APIHandler()
    user_repository = UserRepository(api)

    display_format = get_user_input()
    print(f"Selected display format: {display_format}")

    display_factory = DisplayFactory()
    display_strategy = display_factory.get_display_strategy(display_format)  # Отримуємо стратегію
    
    if action == 'get':
        endpoint = input("Enter endpoint (e.g., posts, users): ")
        if endpoint == "users":
            data = user_repository.get_users()
        elif endpoint == "posts":
            data = user_repository.get_posts()
        else:
            print("Invalid endpoint.")
            return
        
        if data:  
            display_strategy.display(data)
            result = f"Data received successfully, displaying as {display_format}."
        else:
            result = "No data received."
            print(result)
        
        log_request("GET", endpoint, data, display_format, result)


    elif action == 'history':
        show_history()


    elif action == 'save':
        file_format = input("Enter format to save data (json/csv/txt): ")
        save_data(history, file_format)


   