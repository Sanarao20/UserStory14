import logging
from src.loader import load_data
from src.validator import validate_attendance
from src.processor import calculate_attendance, calculate_payroll
from src.report import generate_reports
import os
os.makedirs("logs", exist_ok=True)
logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run():
    emp_path = "data/employees.csv"
    att_path = "data/attendance.csv"

    employees, attendance = load_data(emp_path, att_path)
    attendance = validate_attendance(employees, attendance)

    summary = calculate_attendance(attendance)
    payroll = calculate_payroll(employees, summary)

    generate_reports(payroll, summary)

if __name__ == "__main__":
    run()