import pytest
from employee_salary_report.parsers.csv_parser import CSVParser

def test_employee_creation_valid():
    # Given & When
    parsed_data = CSVParser("./csv_reports/data1.csv")

    # Then
    assert parsed_data["email"] == email
    assert parsed_data["name"] == name
    assert parsed_data["department"] == department
    assert parsed_data["hours_worked"] == hours_worked
    assert parsed_data["id"] == id
    assert parsed_data["hourly_rate"] == hourly_rate


