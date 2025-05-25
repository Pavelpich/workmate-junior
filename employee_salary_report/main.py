import argparse
import sys
import os
from typing import List
from parsers.csv_parser import CSVParser
from employee_salary_report.output.console_output import  ConsoleOutput
from employee_salary_report.reports.payout_report import PayoutReport
from employee_salary_report.output.json_output import JsonOutput
from models.employee import Employee

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate payout reports from employee CSV files.")
    parser.add_argument(
        "files",
        nargs="+",
        help="List of CSV files to process"
    )
    parser.add_argument(
        "--report",
        choices=["payout"],
        default="payout",
        help="Type of report to generate (default: payout)"
    )
    parser.add_argument(
        "--output",
        choices=["console", "json"],
        default="console",
        help="Output format (default: console)"
    )
    return parser.parse_args()


def driver_func() -> None:
    args = parse_args()

    # Здесь можно внедрить дополнительные используемые форматы вывода
    output_formatters = {
        "console": ConsoleOutput(),
        "json": JsonOutput()
    }
    output_formatter = output_formatters[args.output]

    all_employees: List[Employee] = []
    for file_path in args.files:
        try:
            parser = CSVParser(file_path)
            parsed_data = parser.parse()
            employees = [Employee(**record) for record in parsed_data]
            all_employees.extend(employees)
        except (FileNotFoundError, ValueError, TypeError) as e:
            print(f"Error processing file {file_path}: {e}", file=sys.stderr)
            sys.exit(1)

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