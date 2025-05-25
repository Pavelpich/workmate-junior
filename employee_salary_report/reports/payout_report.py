from typing import List
from employee_salary_report.models.employee import Employee
from .base_report import BaseReport
from collections import defaultdict

class PayoutReport(BaseReport):
    """Report of salaries for list of employees"""

    def generate(self, employees: List[Employee]) -> dict:
        report = defaultdict(lambda: {"employees": [], "total_hours": 0, "total_salary": 0})
        for emp in employees:
            department = emp.department
            employee_data = {
                "name": emp.name,
                "hours": emp.hours_worked,
                "salary": emp.salary,
                "hourly_rate": emp.hourly_rate
            }
            report[department]["employees"].append(employee_data)
            report[department]["total_hours"] += emp.hours_worked
            report[department]["total_salary"] += emp.salary
        return dict(report)