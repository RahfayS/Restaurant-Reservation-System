from utils.register import Registration
from utils.login import Login
from utils.makereservation import MakeReservation
from utils.viewreservation import ViewReservation

def reservation_menu(user_email):
    print("\n===== Reservation Menu =====\n")

    while True:
        try:
            option = int(input(
                "Select Option:\n"
                "1. View Reservation\n"
                "2. Make Reservation\n"
                "3. Modify Reservation\n"
                "4. Cancel Reservation\n"
                "5. Logout\n"
                "Selection: "
            ))
        except ValueError:
            print("\n[ERROR]: Please enter a number from 1 - 5\n")
            continue

        match option:
            case 1:
                vr = ViewReservation(user_email)
                vr.start_view()

            case 2:
                mr = MakeReservation(user_email)
                mr.start_reservation()

            case 3:
                print("\nModifying reservation...")

            case 4:
                print("\nCancelling reservation...")

            case 5:
                print("\nLogging out...")
                return

            case _:
                print("\n[ERROR]: Invalid option, choose 1 - 5")


def main():
    print('==== Restaurant Reservation Menu ====\n')

    while True:
        try:
            option = int(input(
                "Select Menu Option:\n"
                "Register: (press 1)\n"
                "Login: (press 2)\n"
                "Exit (press 3)\n"
                "Selection: "
            ))
        except ValueError:
            print("\n[ERROR]: Please enter a number from 1 - 3\n")
            continue

        if option < 1 or option > 3:
            print(f"\n[ERROR]: {option} is invalid, please select a value from 1 - 3\n")
            continue

        match option:
            case 1:
                r = Registration()
                r.start_registration()

            case 2:
                l = Login()
                user_email = l.start_login()
                if user_email:
                    reservation_menu(user_email)

            case 3:
                print("Exiting...")
                return


if __name__ == "__main__":
    main()