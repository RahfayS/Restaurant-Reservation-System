import os
from datetime import datetime
from utils.config import PROJECT_ROOT

class ModifyReservation:

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

    def start_modify(self):
        print("\n===== Modify Reservation =====\n")

        if not os.path.exists(self.data_path):
            print("No reservation found")
            return

        with open(self.data_path, "r") as f:
            content = f.read().strip()

        if content == "":
            print("No reservation found")
            return

        all_blocks = content.split("----------------------")
        user_blocks = [b for b in all_blocks if f"Email: {self.email}" in b]

        if not user_blocks:
            print("No reservation found")
            return

        for i, block in enumerate(user_blocks, 1):
            print(f"Reservation {i}:")
            print(block.strip())
            print("----------------------")

        while True:
            try:
                choice = int(input(f"\nSelect reservation to modify (1-{len(user_blocks)}): "))
                if 1 <= choice <= len(user_blocks):
                    break
                print(f"[ERROR]: Please enter a number between 1 and {len(user_blocks)}")
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

        selected = user_blocks[choice - 1]

        print("\nWhat would you like to modify?")
        print("1. Number of Days")
        print("2. From Date")
        print("3. To Date")
        print("4. Number of Persons")
        print("5. Number of Rooms")

        while True:
            try:
                field_choice = int(input("Selection: "))
                if 1 <= field_choice <= 5:
                    break
                print("[ERROR]: Please enter a number between 1 and 5")
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

        lines = selected.strip().split("\n")
        updated_lines = []

        for line in lines:
            if field_choice == 1 and line.startswith("Number of Days:"):
                updated_lines.append(f"Number of Days: {self.get_int('New number of days: ')}")
            elif field_choice == 2 and line.startswith("From Date:"):
                updated_lines.append(f"From Date: {self.get_date('New From Date (YYYY-MM-DD): ').date()}")
            elif field_choice == 3 and line.startswith("To Date:"):
                updated_lines.append(f"To Date: {self.get_date('New To Date (YYYY-MM-DD): ').date()}")
            elif field_choice == 4 and line.startswith("Number of Persons:"):
                updated_lines.append(f"Number of Persons: {self.get_int('New number of persons: ')}")
            elif field_choice == 5 and line.startswith("Number of Rooms:"):
                updated_lines.append(f"Number of Rooms: {self.get_int('New number of rooms: ')}")
            else:
                updated_lines.append(line)

        updated_block = "\n".join(updated_lines)

        if field_choice in (2, 3):
            from_date = None
            to_date = None
            for line in updated_lines:
                if line.startswith("From Date:"):
                    from_date = datetime.strptime(line.split(": ", 1)[1].strip(), "%Y-%m-%d")
                elif line.startswith("To Date:"):
                    to_date = datetime.strptime(line.split(": ", 1)[1].strip(), "%Y-%m-%d")
            if from_date and to_date and to_date <= from_date:
                print("\n[ERROR]: To Date must be after From Date. Modification cancelled.\n")
                return

        for i, block in enumerate(all_blocks):
            if block == selected:
                all_blocks[i] = updated_block
                break

        with open(self.data_path, "w") as f:
            for block in all_blocks:
                if block.strip():
                    f.write("----------------------\n")
                    f.write(block.strip() + "\n")

        print("\nReservation updated successfully!\n")
