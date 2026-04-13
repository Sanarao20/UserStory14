import pandas as pd
import logging


def calculate_attendance(attendance):

    # Convert P/A → PRESENT/ABSENT
    attendance['status'] = attendance['status'].replace({
        'P': 'PRESENT',
        'A': 'ABSENT'
    })

    summary = attendance.groupby(['employee_id', 'status']).size().unstack(fill_value=0)

    # Ensure both columns exist
    if 'PRESENT' not in summary.columns:
        summary['PRESENT'] = 0

    if 'ABSENT' not in summary.columns:
        summary['ABSENT'] = 0

    summary.rename(columns={
        'PRESENT': 'total_present_days',
        'ABSENT': 'total_absent_days'
    }, inplace=True)

    summary.reset_index(inplace=True)

    logging.info("Attendance calculated")
    return summary


def calculate_payroll(employees, summary):
    df = pd.merge(employees, summary, on='employee_id', how='left').fillna(0)

    df['deduction'] = (df['monthly_salary'] / 30) * df['total_absent_days']
    df['final_salary'] = df['monthly_salary'] - df['deduction']

    logging.info("Payroll calculated")
    return df