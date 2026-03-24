import os
from datetime import datetime
from typing import Dict, Any
from utils.config import PROJECT_ROOT
from utils.custom_exceptions import InvalidDateRangeError


class MakeReservation:
    """
    Handles the process of creating and saving a user reservation.
    """

    def __init__(self, email: str) -> None:
        """
        Initialize the reservation handler with a user's email.
        """
        # Store user email and set file path for reservation storage
        self.email: str = email
        self.data_path: str = os.path.join(PROJECT_ROOT, "user_data", "user_reservation.txt")

    def get_int(self, prompt: str) -> int:
        """
        Prompt the user until a valid integer is entered.
        """
        # Prompt user until a valid integer is entered
        while True:
            value: str = input(prompt).strip()
            if value == "":
                print("[ERROR]: Input cannot be blank.")
                continue
            try:
                return int(value)
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

    def get_date(self, prompt: str) -> datetime:
        """
        Prompt the user until a valid date in YYYY-MM-DD format is entered.
        """
        # Prompt user until a valid date in YYYY-MM-DD format is entered
        while True:
            value: str = input(prompt).strip()
            if value == "":
                print("[ERROR]: Date cannot be blank.")
                continue
            try:
                return datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                print("[ERROR]: Invalid date format. Use YYYY-MM-DD.")

    def save_reservation(self, reservation: Dict[str, Any]) -> None:
        """
        Save the reservation details to a file.
        """
        # Append reservation details to the file
        with open(self.data_path, "a") as f:
            f.write("----------------------\n")
            f.write(f"Email: {self.email}\n")
            f.write(f"Number of Days: {reservation['days']}\n")
            f.write(f"From Date: {reservation['from']}\n")
            f.write(f"To Date: {reservation['to']}\n")
            f.write(f"Number of Persons: {reservation['persons']}\n")
            f.write(f"Number of Rooms: {reservation['rooms']}\n")

    def start_reservation(self) -> None:
        """
        Execute the full reservation workflow, including input collection,
        validation, confirmation, and saving.
        """
        # Main flow for creating a reservation
        print("\n===== Make a Reservation =====\n")

        num_days: int = self.get_int("Number of days: ")
        from_date: datetime = self.get_date("From Date (YYYY-MM-DD): ")
        to_date: datetime = self.get_date("To Date (YYYY-MM-DD): ")

        # Validate date range
        try:
            if to_date <= from_date:
                raise InvalidDateRangeError()
        except InvalidDateRangeError as e:
            print(f"\n{e}\n")
            return

        num_persons: int = self.get_int("Number of Persons: ")
        num_rooms: int = self.get_int("Number of Rooms: ")

        # Display reservation summary
        print("\nReview Your Reservation:")
        print(f"Days: {num_days}")
        print(f"From: {from_date.date()}")
        print(f"To: {to_date.date()}")
        print(f"Persons: {num_persons}")
        print(f"Rooms: {num_rooms}")

        confirm: str = input("\nPress 'Y' to Reserve or any other key to cancel: ").strip().lower()

        if confirm != "y":
            print("\nReservation cancelled.")
            return

        # Build reservation dictionary
        reservation: Dict[str, Any] = {
            "days": num_days,
            "from": from_date.date(),
            "to": to_date.date(),
            "persons": num_persons,
            "rooms": num_rooms
        }

        # Save reservation to file
        self.save_reservation(reservation)

        print("\nReservation Saved Successfully!\n")