import pytest

def test_employee_salary_calculation():
    # Given
    employee = Employee(email="eva@mail.com", hours_worked=150, hourly_rate=40)

    # When
    payout = employee.calculate_salary()

    # Then
    assert payout == 6000