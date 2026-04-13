import logging

def generate_reports(payroll, summary):
    payroll.to_csv("payroll_report.csv", index=False)
    summary.to_csv("attendance_summary.csv", index=False)

    logging.info("Reports generated")