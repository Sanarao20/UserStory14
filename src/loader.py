import pandas as pd
import logging

def load_data(emp_path, att_path):
    try:
        employees = pd.read_csv(emp_path)
        attendance = pd.read_csv(att_path)
        logging.info("Data loaded successfully")
        return employees, attendance
    except Exception as e:
        logging.error(f"Error loading data: {e}")
        raise