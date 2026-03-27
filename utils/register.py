import os
from datetime import datetime
from utils.custom_exceptions import InvalidDobError
from utils.config import PROJECT_ROOT

class Registration:
    """Handles new user registration and saves data to the users file."""
    def __init__(self)->None:
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.__password = ""
        self.dob = ""
    
    def validate_input(self, prompt:str)->str:
        """Helper to validate input is not empty"""
        while True:
            value = input(f'Please enter {prompt}: ').strip()

            if value == "":
                print(f"[ERROR]: Please fill {prompt} data")
                continue

            if value.isnumeric():
                print(f"[ERROR]: {prompt} cannot be a number, please try again")
                continue

            return value

    def get_email(self)->str:
        """Validate and return email"""
        return self.validate_input("Email")
    
    def get_first_name(self)->str:
        """Validate and return first name"""
        while True:
            name = self.validate_input("first name")

            if not name.isalpha():
                print('[ERROR]: First name must only contain letters')
                continue

            return name
    
    def get_last_name(self)->str:
        """Validate and return first name"""
        while True:
            name = self.validate_input("last name")

            if not name.isalpha():
                print('[ERROR]: Last name must only contain letters')
                continue
            
            return name
    
    def get_password(self)->str:
        """Validate and return first name"""
        return self.validate_input("password")

    def get_dob(self)->str:
        """Validate and return first name"""
        while True:
            dob = self.validate_input("date of birth (YYYY-MM-DD)")

            try:
                datetime.strptime(dob, "%Y-%m-%d")
            except InvalidDobError as e:
                print(f'[ERROR]: {e}')
                continue
            except Exception as e:
                print(f'[ERROR]: {e}')
                continue
            else:
                return dob
    
    def save_user(self)->None:
        """Save user data to user_data directory"""
        data_path = os.path.join(PROJECT_ROOT, "user_data")
        os.makedirs(data_path, exist_ok=True)

        with open(os.path.join(data_path, "users_registration.txt"), 'a') as f:
            f.write(
                f"\n----------------------"
                f"\nEmail: {self.email}\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Password: {self.__password}\n"
                f"Date of Birth: {self.dob}\n"
                f"----------------------\n"
            )

    def start_registration(self)->None:
        """
        Run the full registration flow.
        If the DOB is invalid, registration is cancelled and the user is
        returned to wherever they came from.
        """
        print("\n===== Registration In-Process =====\n")

        self.email = self.get_email()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.__password = self.get_password()

        try:
            self.dob = self.get_dob()
        except InvalidDobError as e:
            print(f"\n{e}\n")
            return

        while True:
            print('\nSubmit (press s)')
            print("Exit (press e)")

            selection = input("Select option: ").strip().lower()

            match selection:
                case "s":
                    self.save_user()
                    print("Registration Successful")
                    break
                case "e":
                    print("Registration Cancelled")
                    return
                case _:
                    print("[ERROR]: Invalid Option, please try again")