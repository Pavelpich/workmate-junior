import argparse
import sys
import os
from typing import List
from parsers.csv_parser import CSVParser
from employee_salary_report.output.console_output import  ConsoleOutput
from employee_salary_report.reports.payout_report import PayoutReport
from employee_salary_report.output.json_output import JsonOutput
from models.employee import Employee


def driver_func():
    parser = argparse.ArgumentParser(description="Generate payout reports from employee CSV files.")

    # Здесь можно внедрить дополнительные используемые форматы вывода
    output_formatters = {
        "console": ConsoleOutput(),
        "json": JsonOutput()
    }
    output_formatter = output_formatters[args.output]

    # Сюда можно внедрить дополнительные типы отчетов
    report_types = {
        "payout": PayoutReport()
    }
    report = report_types[args.report]
    report_data = report.generate(all_employees)

    result = output_formatter.render(report_data)
    print(result)


if __name__ == "__main__":
    driver_func()