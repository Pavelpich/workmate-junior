import pytest
from employee_salary_report.reports.payout_report import PayoutReport
from employee_salary_report.models.employee import Employee


def test_generate_report_with_multiple_departments():
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

    # When
    report = PayoutReport()
    result = report.generate(employees)

    # Then
    assert "Marketing" in result
    assert "Design" in result

    marketing = result["Marketing"]
    assert len(marketing["employees"]) == 2
    assert marketing["employees"][0]["name"] == "Alice"
    assert marketing["employees"][0]["hours"] == 160.0
    assert marketing["employees"][0]["salary"] == 8000.0
    assert marketing["employees"][1]["name"] == "Carol"
    assert marketing["employees"][1]["hours"] == 170.0
    assert marketing["employees"][1]["salary"] == 8500.0
    assert marketing["total_hours"] == 330.0
    assert marketing["total_salary"] == 16500.0

    design = result["Design"]
    assert len(design["employees"]) == 1
    assert design["employees"][0]["name"] == "Bob"
    assert design["employees"][0]["hours"] == 150.0
    assert design["employees"][0]["salary"] == 6000.0
    assert design["total_hours"] == 150.0
    assert design["total_salary"] == 6000.0


def test_generate_report_with_single_department():
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
            department="Marketing",
            hours_worked=150,
            hourly_rate=40,
        ),
    ]

    # When
    report = PayoutReport()
    result = report.generate(employees)

    # Then
    assert "Marketing" in result
    assert len(result) == 1

    marketing = result["Marketing"]
    assert len(marketing["employees"]) == 2
    assert marketing["employees"][0]["name"] == "Alice"
    assert marketing["employees"][0]["hours"] == 160.0
    assert marketing["employees"][0]["salary"] == 8000.0
    assert marketing["employees"][1]["name"] == "Bob"
    assert marketing["employees"][1]["hours"] == 150.0
    assert marketing["employees"][1]["salary"] == 6000.0
    assert marketing["total_hours"] == 310.0
    assert marketing["total_salary"] == 14000.0


def test_generate_report_with_empty_list():
    # Given
    employees = []

    # When
    report = PayoutReport()
    result = report.generate(employees)

    # Then
    assert result == {}


def test_generate_report_with_zero_values():
    # Given
    employees = [
        Employee(
            id=1,
            email="alice@example.com",
            name="Alice",
            department="Marketing",
            hours_worked=0,
            hourly_rate=50,
        ),
        Employee(
            id=2,
            email="bob@example.com",
            name="Bob",
            department="Design",
            hours_worked=150,
            hourly_rate=0,
        ),
    ]

    # When
    report = PayoutReport()
    result = report.generate(employees)

    # Then
    assert "Marketing" in result
    assert "Design" in result

    marketing = result["Marketing"]
    assert len(marketing["employees"]) == 1
    assert marketing["employees"][0]["name"] == "Alice"
    assert marketing["employees"][0]["hours"] == 0.0
    assert marketing["employees"][0]["salary"] == 0.0
    assert marketing["total_hours"] == 0.0
    assert marketing["total_salary"] == 0.0

    design = result["Design"]
    assert len(design["employees"]) == 1
    assert design["employees"][0]["name"] == "Bob"
    assert design["employees"][0]["hours"] == 150.0
    assert design["employees"][0]["salary"] == 0.0
    assert design["total_hours"] == 150.0
    assert design["total_salary"] == 0.0
