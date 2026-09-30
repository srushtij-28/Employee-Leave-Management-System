from config import EMPLOYEE_FILE, LEAVE_FILE
from storage import load_data, save_data
from utils import find_employee, generate_leave_id, get_date


def apply_leave():
    employees = load_data(EMPLOYEE_FILE)
    leaves = load_data(LEAVE_FILE)

    employee_id = input("Enter Employee ID: ").strip()

    employee = find_employee(employees, employee_id)

    if not employee:
        print("Employee not found.")
        return

    print(f"\nEmployee: {employee['name']}")
    print(f"Available Leave: {employee['leave_balance']} days")

    try:
        days = int(input("Enter number of leave days: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if days <= 0:
        print("Leave days must be greater than zero.")
        return

    if days > employee["leave_balance"]:
        print("Insufficient leave balance.")
        return

    reason = input("Enter leave reason: ").strip()

    if not reason:
        print("Leave reason cannot be empty.")
        return

    leave = {
        "id": generate_leave_id(leaves),
        "employee_id": employee["id"],
        "employee_name": employee["name"],
        "days": days,
        "reason": reason,
        "date": get_date(),
        "status": "Pending"
    }

    leaves.append(leave)

    save_data(LEAVE_FILE, leaves)

    print(f"Leave request created: {leave['id']}")


def view_leaves():
    leaves = load_data(LEAVE_FILE)

    if not leaves:
        print("No leave requests found.")
        return

    print("\n" + "=" * 85)
    print("LEAVE REQUESTS")
    print("=" * 85)

    for leave in leaves:
        print(
            f"ID: {leave['id']} | "
            f"Employee: {leave['employee_name']} | "
            f"Days: {leave['days']} | "
            f"Status: {leave['status']} | "
            f"Date: {leave['date']}"
        )

        print(f"Reason: {leave['reason']}")
        print("-" * 85)


def approve_leave():
    employees = load_data(EMPLOYEE_FILE)
    leaves = load_data(LEAVE_FILE)

    leave_id = input("Enter Leave ID: ").strip()

    leave = None

    for item in leaves:
        if item["id"].lower() == leave_id.lower():
            leave = item
            break

    if not leave:
        print("Leave request not found.")
        return

    if leave["status"] != "Pending":
        print("This leave request has already been processed.")
        return

    employee = find_employee(employees, leave["employee_id"])

    if not employee:
        print("Employee no longer exists.")
        return

    if leave["days"] > employee["leave_balance"]:
        print("Employee does not have enough leave balance.")
        return

    leave["status"] = "Approved"

    employee["leave_balance"] -= leave["days"]

    save_data(LEAVE_FILE, leaves)
    save_data(EMPLOYEE_FILE, employees)

    print("Leave approved successfully.")


def reject_leave():
    leaves = load_data(LEAVE_FILE)

    leave_id = input("Enter Leave ID: ").strip()

    leave = None

    for item in leaves:
        if item["id"].lower() == leave_id.lower():
            leave = item
            break

    if not leave:
        print("Leave request not found.")
        return

    if leave["status"] != "Pending":
        print("This leave request has already been processed.")
        return

    leave["status"] = "Rejected"

    save_data(LEAVE_FILE, leaves)

    print("Leave rejected successfully.")


def employee_leave_history():
    leaves = load_data(LEAVE_FILE)

    employee_id = input("Enter Employee ID: ").strip()

    results = [
        leave
        for leave in leaves
        if leave["employee_id"].lower() == employee_id.lower()
    ]

    if not results:
        print("No leave history found.")
        return

    print("\nLeave History")

    for leave in results:
        print(
            f"{leave['id']} | "
            f"{leave['days']} days | "
            f"{leave['status']} | "
            f"{leave['date']} | "
            f"{leave['reason']}"
        )
