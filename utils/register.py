import os
from datetime import datetime
from utils.custom_exceptions import InvalidDobError
from utils.config import PROJECT_ROOT
class Registration:
    def __init__(self):
        self.email = ""
        self.first_name = ""
        self.last_name = ""
        self.__password = ""
        self.dob = ""
    
    def validate_input(self,prompt):
        """Helper to validate input is not empty"""
        while True:
            # --- Get Input ---
            value = input(f'Please enter {prompt}: ').strip()
            # --- Verify input is not empty ---
            if value == "":
                print(f"[ERROR]: Please fill {prompt} data")
                continue

            # --- Verify input is not a numeric ---
            if value.isnumeric():
                print(f"[ERROR]: {prompt} cannot be a number, please try again")
                continue

            return value
            



    def get_email(self):
        """Helper to get email and validate"""
        return self.validate_input("Email")
    
    def get_first_name(self):
        """Helper to get first name and validate"""
        while True:
            name = self.validate_input("first name")

            # --- Verify name has only letters ---
            if not name.isalpha():
                print(f'[ERROR]: First name must only contain letters')
                continue

            return name
    
    def get_last_name(self):
        """Helper to get last name and validate"""
        while True:
            name = self.validate_input("last name")

            # --- Verify name has only letters ---
            if not name.isalpha():
                print(f'[ERROR]: Last name must only contain letters')
                continue
            
            return name
    
    def get_password(self):
        """Helper to get password and validate"""
        return self.validate_input("password")

    def get_dob(self):
        """Helper to get date of birth and validate"""
        while True:
            dob = self.validate_input("date of birth (YYYY-MM-DD)")

            # --- Ensure dob follows (YYYY-MM-DD) Format ---
            try:
                datetime.strptime(dob,"%Y-%m-%d") # Try to parse the users dob, if it fails its not in valid format
            except ValueError :
                raise InvalidDobError()
                
            else:
                return dob
    
    def save_user(self):
        """Helper to save user data to user_data directory"""
        # --- Create directory ---
        data_path = os.path.join(PROJECT_ROOT,"user_data")
        os.makedirs(data_path,exist_ok=True)
        # --- Save directory ---
        with open(os.path.join(data_path,"users_registration.txt"),'a') as f:
            f.write(
                f"\n----------------------"
                f"\nEmail: {self.email}\n"
                f"First name: {self.first_name}\n"
                f"Last name: {self.last_name}\n"
                f"Password: {self.__password}\n"
                f"Date of Birth: {self.dob}\n"
                f"----------------------\n"
        )
    def start_registration(self):
        """Entry point for registration process"""
        print("\n===== Registration In-Process =====\n")

        # --- Get User Data ---
        self.email = self.get_email()
        self.first_name = self.get_first_name()
        self.last_name = self.get_last_name()
        self.__password = self.get_password()
        self.dob = self.get_dob()
        

        # --- Further Actions ---
        while True:
            print('\nSubmit (press s)')
            print("Exit (press e)")

            # --- Get User Selection (Exit or Submit) ---
            selection = input("Select option: ").strip().lower()

            # --- Match Selection ---
            match selection:
                case "s": # User wants to submit
                    self.save_user()
                    print("Registration Successful")
                    break
                case "e":
                    print("Registration Cancelled")
                    return
                case _:
                    print("[ERROR]: Invalid Option, please try again")


