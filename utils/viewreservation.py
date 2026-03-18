import os
from utils.config import PROJECT_ROOT

class ViewReservation:

    def __init__(self, email):
        self.email = email
        self.data_path = os.path.join(PROJECT_ROOT, "user_data", "user_reservation.txt")

    def start_view(self):
        print("\n===== Your Reservations =====\n")

        if not os.path.exists(self.data_path):
            print("No reservation found")
            return

        with open(self.data_path, "r") as f:
            content = f.read().strip()

        if content == "":
            print("No reservation found")
            return

        reservations = content.split("----------------------")

        found = False

        for r in reservations:
            if f"Email: {self.email}" in r:
                print(r.strip())
                print("----------------------")
                found = True

        if not found:
            print("No reservation found")