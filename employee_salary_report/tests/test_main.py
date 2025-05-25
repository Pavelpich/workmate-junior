import pytest
import sys
from main import parse_args, validate_files, main
from parsers.csv_parser import CSVParser
from employee_salary_report.output.console_output import  ConsoleOutput
from employee_salary_report.reports.payout_report import PayoutReport
from employee_salary_report.output.json_output import JsonOutput

def test_parse_args_with_all_arguments():
    # Given
    sys.argv = ["main.py", "file1.csv", "file2.csv", "--report", "payout", "--output", "json"]

    # When
    args = parse_args()

    # Then
    assert args.files == ["file1.csv", "file2.csv"]
    assert args.report == "payout"
    assert args.output == "json"
