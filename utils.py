from datetime import datetime


def get_date():
    return datetime.now().strftime("%Y-%m-%d")


def generate_leave_id(leaves):
    if not leaves:
        return "L001"

    numbers = []

    for leave in leaves:
        leave_id = leave.get("id", "")

        if leave_id.startswith("L"):
            try:
                numbers.append(int(leave_id[1:]))
            except ValueError:
                pass

    next_number = max(numbers, default=0) + 1

    return f"L{next_number:03d}"


def find_employee(employees, employee_id):
    for employee in employees:
        if employee["id"].lower() == employee_id.lower():
            return employee

    return None
