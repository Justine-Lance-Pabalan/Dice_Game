from .dice_game import DiceGame
from .user import User

DG_i = DiceGame()

class UserManager:
    Users = {}

    def __init__(self):
        self.load_users()  # FIX: load users on startup so registered users persist between sessions

    def load_users(self):  # FIX: added 'self' parameter
        try:
            with open("users.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    username, password = line.strip().split(',')
                    UserManager.Users[username] = User(username, password)
        except FileNotFoundError:
            print("No user data found.")

    def save_users(self):  # FIX: added 'self' parameter
        with open("users.txt", "w") as f:
            for username, user in UserManager.Users.items():
                f.write(f"{username},{user.password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            print("Username must be at least 4 characters long.")
            return False  # FIX: return False instead of recursively calling register()
        elif username in self.Users:
            print("Username already exists.")
            return False
        else:
            return True

    def validate_password(self, password):
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            return False  # FIX: return False instead of recursively calling register()
        else:
            return True

    def register(self):
        print("\nRegistration")
        username = input("Enter username (at least 4 characters), or leave blank to cancel: ")
        if username == "":
            return
        if self.validate_username(username):
            password = input("Enter password (at least 8 characters), or leave blank to cancel: ")
            if password == "":
                return
            if self.validate_password(password):
                print("Registration successful.")
                self.Users[username] = User(username, password)
                self.save_users()  # FIX: added () so the function actually gets called

    def login(self):
        print("\nLogin")
        username = input("Enter username, or leave blank to cancel: ")
        if username == "":
            return
        password = input("Enter password, or leave blank to cancel: ")
        if password == "":
            return
        if username in self.Users:
            if password == self.Users[username].password:
                DG_i.menu(username)
            else:
                print("Invalid username/password.")
                self.login()
        else:
            print("Username does not exist.")
