import os
from datetime import datetime
from utils.config import PROJECT_ROOT

class MakeReservation:

    def __init__(self, email):
        self.email = email
        self.data_path = os.path.join(PROJECT_ROOT, "user_data", "user_reservation.txt")

    def get_int(self, prompt):
        while True:
            value = input(prompt).strip()
            if value == "":
                print("[ERROR]: Input cannot be blank.")
                continue
            try:
                return int(value)
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

    def get_date(self, prompt):
        while True:
            value = input(prompt).strip()
            if value == "":
                print("[ERROR]: Date cannot be blank.")
                continue
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("[ERROR]: Invalid date format. Use YYYY-MM-DD.")

    def save_reservation(self, reservation):
        with open(self.data_path, "a") as f:
            f.write("----------------------\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Number of Days: {reservation['days']}\n")
            f.write(f"From Date: {reservation['from']}\n")
            f.write(f"To Date: {reservation['to']}\n")
            f.write(f"Number of Persons: {reservation['persons']}\n")
            f.write(f"Number of Rooms: {reservation['rooms']}\n")

    def start_reservation(self):
        print("\n===== Make a Reservation =====\n")

        num_days = self.get_int("Number of days: ")
        from_date = self.get_date("From Date (YYYY-MM-DD): ")
        to_date = self.get_date("To Date (YYYY-MM-DD): ")

        if to_date <= from_date:
            print("\n[ERROR]: To Date must be after From Date.\n")
            return

        num_persons = self.get_int("Number of Persons: ")
        num_rooms = self.get_int("Number of Rooms: ")

        print("\nReview Your Reservation:")
        print(f"Days: {num_days}")
        print(f"From: {from_date.date()}")
        print(f"To: {to_date.date()}")
        print(f"Persons: {num_persons}")
        print(f"Rooms: {num_rooms}")

        confirm = input("\nPress 'Y' to Reserve or any other key to cancel: ").strip().lower()

        if confirm != "y":
            print("\nReservation cancelled.")
            return

        reservation = {
            "days": num_days,
            "from": from_date.date(),
            "to": to_date.date(),
            "persons": num_persons,
            "rooms": num_rooms
        }

        self.save_reservation(reservation)

        print("\nReservation Saved Successfully!\n")