import pandas as pd
import logging


def validate_attendance(employees, attendance):
    try:
        # Get valid employee IDs
        valid_emp_ids = set(employees['employee_id'])

        # ✅ Rule 1: employee must exist
        attendance = attendance[
            attendance['employee_id'].isin(valid_emp_ids)
        ]

        # ✅ Rule 2: valid date
        attendance['date'] = pd.to_datetime(
            attendance['date'],
            errors='coerce'
        )

        # Remove invalid dates (NaT)
        attendance = attendance.dropna(subset=['date'])

        logging.info("Attendance validation successful")

        return attendance

    except Exception as e:
        logging.error(f"Validation error: {e}")
        raise