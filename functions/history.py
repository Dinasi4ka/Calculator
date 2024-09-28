from constants.globalVariables import history

def add_to_history(num1, operator, num2, result):
    if num2 is None: 
        history.append(f"{operator}({num1}) = {result}")
    else:
        history.append(f"{num1} {operator} {num2} = {result}")

def show_history():
    if history:
        print("\nІсторія обчислень:")
        for entry in history:
            print(entry)
    else:
        print("Історія порожня.")

def clear_history():
    history.clear()
    print("Історію очищено.")