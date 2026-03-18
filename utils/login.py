import os
from utils.config import PROJECT_ROOT

class Login:
    def __init__(self):
        self.email = ""
        self.password = ""

    def validate_input(self, prompt):
        while True:
            value = input(f"Please enter {prompt}: ").strip()
            if value == "":
                print(f"[ERROR]: {prompt} cannot be empty")
                continue
            return value

    def get_email(self):
        return self.validate_input("Email")

    def get_password(self):
        return self.validate_input("Password")

    def authenticate(self):
        data_path = os.path.join(PROJECT_ROOT, "user_data", "users_registration.txt")

        if not os.path.exists(data_path):
            print("[ERROR]: No registered users found. Please register first.")
            return False

        with open(data_path, "r") as f:
            content = f.read()

        users = content.split("----------------------")

        email_line = f"Email: {self.email}"
        password_line = f"Password: {self.password}"

        for user in users:
            if email_line in user and password_line in user:
                return True

        return False

    def start_login(self):
        print("\n===== Login =====\n")

        self.email = self.get_email()
        self.password = self.get_password()

        if self.authenticate():
            print("\nLogin Successful! Welcome back.")
            return self.email
        else:
            print("\n[ERROR]: Invalid email or password. Please try again.")
            return None