from shered.constants.globalVariables import memory_value, decimal_places

def save_result(result, decimal_places): 
    global memory_value
    if isinstance(result, float):
        result = round(result, decimal_places)
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
