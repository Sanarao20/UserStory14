import unittest
import pandas as pd
from src.validator import validate_attendance
from src.processor import calculate_attendance, calculate_payroll

class TestPayrollEngine(unittest.TestCase):

    def setUp(self):
        self.employees = pd.DataFrame({
            'employee_id': [1, 2],
            'monthly_salary': [3000, 6000]
        })

        self.attendance = pd.DataFrame({
            'employee_id': [1, 1, 2, 3],
            'date': ['2024-01-01', 'invalid', '2024-01-02', '2024-01-03'],
            'status': ['PRESENT', 'ABSENT', 'ABSENT', 'PRESENT']
        })

    def test_invalid_employee_rejected(self):
        validated = validate_attendance(self.employees, self.attendance)
        self.assertNotIn(3, validated['employee_id'].values)

    def test_invalid_date_ignored(self):
        validated = validate_attendance(self.employees, self.attendance)
        self.assertEqual(len(validated), 2)

    def test_attendance_count(self):
        validated = validate_attendance(self.employees, self.attendance)
        summary = calculate_attendance(validated)
        self.assertIn('total_present_days', summary.columns)

    def test_salary_deduction(self):
        validated = validate_attendance(self.employees, self.attendance)
        summary = calculate_attendance(validated)
        payroll = calculate_payroll(self.employees, summary)

        emp2 = payroll[payroll['employee_id'] == 2].iloc[0]
        self.assertEqual(emp2['deduction'], 6000/30)

    def test_final_salary_calculation(self):
        validated = validate_attendance(self.employees, self.attendance)
        summary = calculate_attendance(validated)
        payroll = calculate_payroll(self.employees, summary)

        emp2 = payroll[payroll['employee_id'] == 2].iloc[0]
        self.assertEqual(emp2['final_salary'], 6000 - (6000/30))


if __name__ == "__main__":
    unittest.main()