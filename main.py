import os

from config import DATA_DIR, EMPLOYEE_FILE, LEAVE_FILE
from storage import save_data

from employee_manager import (
    add_employee,
    view_employees,
    search_employee,
    delete_employee,
    show_leave_balance
)

from leave_manager import (
    apply_leave,
    view_leaves,
    approve_leave,
    reject_leave,
    employee_leave_history
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(EMPLOYEE_FILE):
        save_data(EMPLOYEE_FILE, [])

    if not os.path.exists(LEAVE_FILE):
        save_data(LEAVE_FILE, [])


def show_menu():
    print("\n")
    print("=" * 50)
    print("       EMPLOYEE LEAVE MANAGEMENT SYSTEM")
    print("=" * 50)

    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Check Leave Balance")
    print("6. Apply Leave")
    print("7. View Leave Requests")
    print("8. Approve Leave")
    print("9. Reject Leave")
    print("10. Employee Leave History")
    print("11. Exit")

    print("=" * 50)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            delete_employee()

        elif choice == "5":
            show_leave_balance()

        elif choice == "6":
            apply_leave()

        elif choice == "7":
            view_leaves()

        elif choice == "8":
            approve_leave()

        elif choice == "9":
            reject_leave()

        elif choice == "10":
            employee_leave_history()

        elif choice == "11":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
