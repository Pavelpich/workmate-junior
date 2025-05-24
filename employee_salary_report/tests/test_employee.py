import pytest
from ..models.employee import Employee


def test_employee_creation_valid():
    # Given
    email = "eva@mail.com"
    name = "Eva"
    department = "IT"
    hours_worked = 150
    id = 0
    hourly_rate = 40

    # When
    employee = Employee(
        email=email,
        name=name,
        department=department,
        hours_worked=hours_worked,
        id=id,
        hourly_rate=hourly_rate,
    )

    # Then
    assert employee.email == email
    assert employee.name == name
    assert employee.department == department
    assert employee.hours_worked == hours_worked
    assert employee.id == id
    assert employee.hourly_rate == hourly_rate


def test_employee_salary_calculation():
    # Given
    employee = Employee(
        email="eva@mail.com",
        name="Eva",
        department="IT",
        hours_worked=150,
        id=0,
        hourly_rate=40,
    )

    # When
    salary = employee.salary

    # Then
    assert salary == 6000


def test_employee_salary_float():
    # Given
    employee = Employee(email="ivan@mail.com", hours_worked=100, hourly_rate=36.64)

    # When
    salary = employee.salary

    # Then
    assert salary == 3664


def test_employee_with_empty_email_raises_error():
    # Given
    email = ""
    name = "Eva"
    department = "IT"
    hours_worked = 150
    id = 0
    hourly_rate = 40

    # When&Then
    with pytest.raises(ValueError):
        Employee(
            email=email,
            name=name,
            department=department,
            hours_worked=hours_worked,
            id=id,
            hourly_rate=hourly_rate,
        )


def test_employee_with_empty_department_raises_error():
    # Given
    email = "eva@mail.com"
    name = "Eva"
    department = ""
    hours_worked = 150
    id = 0
    hourly_rate = 40

    # When&Then
    with pytest.raises(ValueError):
        Employee(
            email=email,
            name=name,
            department=department,
            hours_worked=hours_worked,
            id=id,
            hourly_rate=hourly_rate,
        )


def test_employee_with_empty_name_raises_error():
    # Given
    email = "eva@mail.com"
    name = ""
    department = "IT"
    hours_worked = 150
    id = 0
    hourly_rate = 40

    # When&Then
    with pytest.raises(ValueError):
        Employee(
            email=email,
            name=name,
            department=department,
            hours_worked=hours_worked,
            id=id,
            hourly_rate=hourly_rate,
        )


def test_employee_with_negative_hours_raises_error():
    # Given
    email = "eva@mail.com"
    name = ""
    department = "IT"
    hours_worked = 150
    id = 0
    hourly_rate = 40

    # When&Then
    with pytest.raises(ValueError):
        Employee(
            email=email,
            name=name,
            department=department,
            hours_worked=hours_worked,
            id=id,
            hourly_rate=hourly_rate,
        )


def test_employee_with_negative_rate_raises_error():
    # Given
    email = "eva@mail.com"
    name = "Eva"
    department = "IT"
    hours_worked = 150
    id = 0
    hourly_rate = -40

    # When&Then
    with pytest.raises(ValueError):
        Employee(
            email=email,
            name=name,
            department=department,
            hours_worked=hours_worked,
            id=id,
            hourly_rate=hourly_rate,
        )
