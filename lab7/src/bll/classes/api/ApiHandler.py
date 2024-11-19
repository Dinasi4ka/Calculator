import requests

class APIHandler:
    BASE_URL = "https://jsonplaceholder.typicode.com"
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(APIHandler, cls).__new__(cls)
        return cls._instance

    def get_data(self, endpoint):
        response = requests.get(f"{self.BASE_URL}/{endpoint}")
        return response.json()