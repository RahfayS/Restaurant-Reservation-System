import os
from typing import List
from utils.config import PROJECT_ROOT


class CancelReservation:
    """
    Handles the process of viewing and cancelling a user's reservations.
    """
    def __init__(self, email: str) -> None:
        """
        Initialize the cancellation handler with a user's email.
        """
        # Store user email and set file path for reservation storage
        self.email: str = email
        self.data_path: str = os.path.join(PROJECT_ROOT, "user_data", "user_reservation.txt")

    def start_cancel(self) -> None:
        """
        Execute the full cancellation workflow, including displaying
        user reservations, selecting one, confirming, and removing it.
        """
        print("\n===== Cancel Reservation =====\n")

        # Check if reservation file exists
        if not os.path.exists(self.data_path):
            print("No reservation found")
            return

        # Read file content
        with open(self.data_path, "r") as f:
            content: str = f.read().strip()

        # Check if file is empty
        if content == "":
            print("No reservation found")
            return

        # Split reservations into blocks
        all_blocks: List[str] = content.split("----------------------")

        # Filter reservations belonging to the current user
        user_blocks: List[str] = [b for b in all_blocks if f"Email: {self.email}" in b]

        if not user_blocks:
            print("No reservation found")
            return

        # Display user's reservations
        for i, block in enumerate(user_blocks, 1):
            print(f"Reservation {i}:")
            print(block.strip())
            print("----------------------")

        # Prompt user to select a reservation to cancel
        while True:
            try:
                choice: int = int(input(f"\nSelect reservation to cancel (1-{len(user_blocks)}): "))
                if 1 <= choice <= len(user_blocks):
                    break
                print(f"[ERROR]: Please enter a number between 1 and {len(user_blocks)}")
            except ValueError:
                print("[ERROR]: Please enter a valid number.")

        # Identify selected reservation
        selected: str = user_blocks[choice - 1]

        # Confirm cancellation
        confirm: str = input("\nAre you sure you want to cancel this reservation? (Y to confirm): ").strip().lower()

        if confirm != "y":
            print("\nCancellation aborted.")
            return

        # Remove selected reservation from all blocks
        for i, block in enumerate(all_blocks):
            if block == selected:
                all_blocks[i] = ""
                break

        # Rewrite file without the cancelled reservation
        with open(self.data_path, "w") as f:
            for block in all_blocks:
                if block.strip():
                    f.write("----------------------\n")
                    f.write(block.strip() + "\n")

        print("\nReservation cancelled successfully!\n")