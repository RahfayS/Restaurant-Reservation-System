import os
from utils.config import PROJECT_ROOT
from utils.register import Registration
class Login:
    """Handles user authentication against the registered user files"""
    def __init__(self) -> None:
        self.email = ""
        self.__password = ""
        self.registration = Registration()

    def validate_input(self, prompt:str) -> str:
        """Repeatedly prompt until the user provides a non-empty value"""
        while True:
            value = input(f"Please enter {prompt}: ").strip()
            if value == "":
                print(f"[ERROR]: {prompt} cannot be empty")
                continue
            return value

    def get_email(self) -> str:
        """Validate and return the users email"""
        return self.validate_input("Email")

    def get_password(self) -> str:
        """Validate and return users password"""
        return self.validate_input("Password")

    def authenticate(self) -> bool:
        """
        Check the registration file for a matching email + password pair.
        Returns True if found, False otherwise.
        """

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

    def start_login(self) -> str:
        """
        Run the login flow.
        On success, returns the authenticated email.
        On failure, offers the user three choices:
          1. Try again
          2. Register
          3. Exit to main menu
        Returns the email string on success, or None to return to main menu.
        """
        print("\n===== Login =====\n")

        self.email = self.get_email()
        self.password = self.get_password()

        if self.authenticate():
            print("\nLogin Successful! Welcome back.")
            return self.email

        print("\n[ERROR]: The password or username you've entered is incorrect.")

        #  Re-prompt User 
        while True:
            print("\nWhat would you like to do?")
            print("1. Try again (Login)")
            print("2. Register")
            print("3. Exit (Main Menu)")

            try:
                choice = int(input("Selection: ").strip())
            except ValueError:
                print("[ERROR]: Please enter a number from 1 - 3")
                continue

            if choice == 1:
                # Outer loop re-prompts credentials
                break
            elif choice == 2:
                # Launch registration 
                self.registration.start_registration()
            elif choice == 3:
                # Return back to main menu
                return None
            else:
                print("[ERROR]: Please enter a number from 1 - 3")
