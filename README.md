# UserStory14
Employee Attendance &amp; Payroll Processing Engine where it is application to process employee attendance and calculate salary deductions.

# Employee Attendance & Payroll Processing Engine

## Objective
This project is a Python-based application that processes employee attendance data and calculates salary deductions based on absences.

## Features
- Load employee and attendance data from CSV files
- Validate records:
  - Employee must exist
  - Dates must be valid
- Process attendance:
  - Calculate total present days
  - Calculate total absent days
- Payroll processing:
  - Deduction per absent day = monthly_salary / 30
  - Final salary calculation after deductions
- Generate output reports
- Logging for tracking execution
- Unit testing for validation

## Project Structure
```

employee_payroll/
│
├── src/
│   ├── **init**.py
│   ├── loader.py
│   ├── validator.py
│   ├── processor.py
│   ├── report.py
│   └── main.py
│
├── tests/
│   └── test_engine.py
│
├── data/
│   ├── employees.csv
│   └── attendance.csv
│
├── logs/
│   └── app.log
│
├── requirements.txt
└── README.md

````
## Setup Instructions

### 1. Create Virtual Environment
```bash
python3 -m venv venv
````

### 2. Activate Environment

**Mac/Linux:**

```bash
source venv/bin/activate
```

**Windows:**

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

```bash
python3 -m src.main
```

## Running Unit Tests

```bash
python3 -m unittest discover -s tests -v
```

## Input Files

### employees.csv

* employee_id
* employee_name
* department
* monthly_salary

### attendance.csv

* employee_id
* date
* status (P = Present, A = Absent)

## Output Files

### 1. attendance_summary.csv

Contains:

* employee_id
* total_present_days
* total_absent_days

### 2. payroll_report.csv

Contains:

* employee details
* attendance summary
* deduction
* final salary

## Payroll Logic

* Deduction per absent day:

  ```
  monthly_salary / 30
  ```
* Final Salary:

  ```
  monthly_salary - (absent_days * deduction_per_day)
  ```
  
## Data Validation Rules

* Invalid employee IDs are ignored
* Invalid dates are removed
* Missing attendance defaults to 0
* Status values (P/A) are normalized internally

## Logging

* Logs are stored in:

  ```
  logs/app.log
  ```
* Tracks:

  * Data loading
  * Validation
  * Processing
  * Errors

## Unit Tests Covered

* Invalid employee rejection
* Invalid date handling
* Attendance counting
* Salary deduction calculation
* Final salary validation

## Tech Stack

* Python
* Pandas
* Logging
* Unittest

## Use Case

This project simulates a real-world payroll processing system and demonstrates:

* Data validation
* Data processing pipelines
* Modular coding structure
* Testing practices
