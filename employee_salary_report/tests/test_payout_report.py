import pytest

def test_employee_salary_calculation():
    # Given
    employee = Employee(email="eva@mail.com", hours_worked=150, hourly_rate=40)

    # When
    employee.calculate_salary()

    # Then
    assert employee.salary == 6000