from abc import ABC, abstractmethod
from typing import List
from employee_salary_report.models.employee import Employee


class BaseReport(ABC):
    """Abstract class that is inherited to create actual reports"""

    @abstractmethod
    def generate(self, employees: List[Employee]) -> dict:
        raise NotImplementedError
