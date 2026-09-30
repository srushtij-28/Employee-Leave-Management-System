import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

EMPLOYEE_FILE = os.path.join(DATA_DIR, "employees.json")
LEAVE_FILE = os.path.join(DATA_DIR, "leaves.json")

DEFAULT_LEAVE_BALANCE = 12
