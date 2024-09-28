from constants.globalVariables import memory_value

def save_result(result): 
    global memory_value
    memory_value = result
    print(f"Збережено {result} в пам'ять")

def get_result():
    if memory_value is not None:
        return memory_value
    else:
        print("Немає збереженого значення в пам'яті.")
        return None

def has_memory():
    return memory_value is not None