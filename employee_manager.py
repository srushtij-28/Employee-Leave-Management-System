from config import EMPLOYEE_FILE, DEFAULT_LEAVE_BALANCE
from storage import load_data, save_data
from utils import find_employee


def add_employee():
    employees = load_data(EMPLOYEE_FILE)

    employee_id = input("Enter Employee ID: ").strip()

    if find_employee(employees, employee_id):
        print("Employee ID already exists.")
        return

    name = input("Enter Employee Name: ").strip()
    department = input("Enter Department: ").strip()

    if not name or not department:
        print("Name and department cannot be empty.")
        return

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "leave_balance": DEFAULT_LEAVE_BALANCE
    }

    employees.append(employee)

    save_data(EMPLOYEE_FILE, employees)

    print("Employee added successfully.")


def view_employees():
    employees = load_data(EMPLOYEE_FILE)

    if not employees:
        print("No employees found.")
        return

    print("\n" + "=" * 65)
    print("EMPLOYEE LIST")
    print("=" * 65)

    for employee in employees:
        print(
            f"ID: {employee['id']} | "
            f"Name: {employee['name']} | "
            f"Department: {employee['department']} | "
            f"Leave Balance: {employee['leave_balance']}"
        )


def search_employee():
    employees = load_data(EMPLOYEE_FILE)

    keyword = input("Enter employee ID or name: ").strip().lower()

    results = []

    for employee in employees:
        if (
            keyword in employee["id"].lower()
            or keyword in employee["name"].lower()
        ):
            results.append(employee)

    if not results:
        print("No employee found.")
        return

    print("\nSearch Results:")

    for employee in results:
        print(
            f"{employee['id']} | "
            f"{employee['name']} | "
            f"{employee['department']} | "
            f"Balance: {employee['leave_balance']}"
        )


def delete_employee():
    employees = load_data(EMPLOYEE_FILE)

    employee_id = input("Enter Employee ID to delete: ").strip()

    employee = find_employee(employees, employee_id)

    if not employee:
        print("Employee not found.")
        return

    employees.remove(employee)

    save_data(EMPLOYEE_FILE, employees)

    print("Employee deleted successfully.")


def show_leave_balance():
    employees = load_data(EMPLOYEE_FILE)

    employee_id = input("Enter Employee ID: ").strip()

    employee = find_employee(employees, employee_id)

    if not employee:
        print("Employee not found.")
        return

    print(f"\nEmployee: {employee['name']}")
    print(f"Leave Balance: {employee['leave_balance']} days")
