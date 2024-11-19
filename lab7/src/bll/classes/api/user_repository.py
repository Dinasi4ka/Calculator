from src.bll.classes.api.ApiHandler import APIHandler

class UserRepository:
    def __init__(self, api_handler):
        self.api_handler = api_handler

    def get_users(self):
        return self.api_handler.get_data("users")

    def get_posts(self):
        return self.api_handler.get_data("posts")