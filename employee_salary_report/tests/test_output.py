import pytest
from employee_salary_report.output.console_output import ConsoleOutput
from employee_salary_report.reports.payout_report import PayoutReport
from employee_salary_report.output.json_output import JsonOutput
from employee_salary_report.models.employee import Employee


def test_console_output_renders_correctly():
    # Given
    employees = [
        Employee(
            id=1,
            email="alice@example.com",
            name="Alice",
            department="Marketing",
            hours_worked=160,
            hourly_rate=50,
        ),
        Employee(
            id=2,
            email="bob@example.com",
            name="Bob",
            department="Design",
            hours_worked=150,
            hourly_rate=40,
        ),
        Employee(
            id=3,
            email="carol@example.com",
            name="Carol",
            department="Marketing",
            hours_worked=170,
            hourly_rate=50,
        ),
    ]
    report = PayoutReport()
    data = report.generate(employees)
    console_output = ConsoleOutput()

    # When
    result = console_output.render(data)

    # Then
    expected = """Payout Report
\Department: Marketing
Employee             Hours      Hourly Rate       Salary
-------------------------------------------------------
Alice               160.00            50.00      8000.00
Carol               170.00            50.00      8500.00
-------------------------------------------------------
Total               330.00                      16500.00
\Department: Design
Employee             Hours      Hourly Rate       Salary
-------------------------------------------------------
Bob                 150.00            40.00      6000.00
-------------------------------------------------------
Total               150.00                       6000.00
"""
    assert result == expected


def test_console_output_with_empty_data():
    # Given
    employees = []
    report = PayoutReport()
    data = report.generate(employees)
    console_output = ConsoleOutput()

    # When
    result = console_output.render(data)

    # Then
    expected = "Payout Report\n"
    assert result == expected


# Tests for JsonOutput
def test_json_output_renders_correctly():
    # Given
    employees = [
        Employee(
            id=1,
            email="alice@example.com",
            name="Alice",
            department="Marketing",
            hours_worked=160,
            hourly_rate=50,
        ),
        Employee(
            id=2,
            email="bob@example.com",
            name="Bob",
            department="Design",
            hours_worked=150,
            hourly_rate=40,
        ),
        Employee(
            id=3,
            email="carol@example.com",
            name="Carol",
            department="Marketing",
            hours_worked=170,
            hourly_rate=50,
        ),
    ]
    report = PayoutReport()
    data = report.generate(employees)
    json_output = JsonOutput()

    # When
    result = json_output.render(data)

    # Then
    expected = """{
  "Marketing": {
    "employees": [
      {
        "name": "Alice",
        "hours": 160,
        "salary": 8000,
        "hourly_rate": 50
      },
      {
        "name": "Carol",
        "hours": 170,
        "salary": 8500,
        "hourly_rate": 50
      }
    ],
    "total_hours": 330,
    "total_salary": 16500
  },
  "Design": {
    "employees": [
      {
        "name": "Bob",
        "hours": 150,
        "salary": 6000,
        "hourly_rate": 40
      }
    ],
    "total_hours": 150,
    "total_salary": 6000
  }
}"""
    assert result.strip() == expected.strip()


def test_json_output_with_empty_data():
    # Given
    employees = []
    report = PayoutReport()
    data = report.generate(employees)
    json_output = JsonOutput()

    # When
    result = json_output.render(data)

    # Then
    expected = "{}"
    assert result == expected
