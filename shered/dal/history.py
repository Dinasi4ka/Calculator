from shered.constants.globalVariables import history, decimal_places

def add_to_history(operand1, operator, operand2, result):
    if operand2 is None: 
        history.append(f"{operator}({operand1}) = {result}")
    else:
        history.append(f"{operand1} {operator} {operand2} = {result}")

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