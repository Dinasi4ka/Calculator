import pandas as pd

class DataRepository:
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            data = pd.read_csv(self.file_path)
            data['date'] = pd.to_datetime(data['date'])  
            return data
        except FileNotFoundError:
            print("Файл не знайдено!")
            return pd.DataFrame()

    def get_data(self):
        return self.data