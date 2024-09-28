from constants.globalVariables import decimal_places

def update_settings():
    global decimal_places
    decimal_places = input("Введіть кількість десяткових розрядів (за замовчуванням 2): ")
    if not decimal_places.isdigit():
        decimal_places = 2
    else:
         decimal_places = int(decimal_places)
    
    return {
        "decimal_places": decimal_places
    }

       
    
  
       


