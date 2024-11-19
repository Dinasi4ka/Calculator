class DataProcessingStrategy:
    
    def process(self, data):
        raise NotImplementedError("Метод повинен бути реалізований у підкласах")

class ExtremeValuesStrategy(DataProcessingStrategy):
    
    def process(self, data):
        extreme_values = data.agg(['min', 'max'])
        return extreme_values