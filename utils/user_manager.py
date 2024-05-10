from .user import User
import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.load_users()
        
    def load_users(self):
        if not os.path.exist("data"):
            os.maskedir("data")
        try:
            with open("data/users.txt" , "r") as file:
                for lime in file:
                    username, password = line.strip().split("|")
                    self.users[username] = password
        except FileNotFoundError:
            return None
        except ValueError:
            return None
            