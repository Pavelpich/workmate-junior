import pytest
import sys
from employee_salary_report.main import parse_args, driver_func

# Define paths to existing CSV files
DATA1_PATH = "./csv_reports/data1.csv"
DATA2_PATH = "./csv_reports/data2.csv"
DATA3_PATH = "./csv_reports/data3.csv"


# Argument Parsing Tests
def test_parse_args_with_all_arguments():
    sys.argv = [
        "main.py",
        DATA1_PATH,
        DATA2_PATH,
        "--report",
        "payout",
        "--output",
        "json",
    ]
    args = parse_args()
    assert args.files == [DATA1_PATH, DATA2_PATH]
    assert args.report == "payout"
    assert args.output == "json"


def test_parse_args_with_defaults():
    sys.argv = ["main.py", DATA1_PATH]
    args = parse_args()
    assert args.files == [DATA1_PATH]
    assert args.report == "payout"
    assert args.output == "console"


def test_parse_args_invalid_report():
    sys.argv = ["main.py", DATA1_PATH, "--report", "invalid"]
    with pytest.raises(SystemExit):
        driver_func()


def test_parse_args_invalid_format_output():
    sys.argv = ["main.py", DATA1_PATH, "--output", "xml"]
    with pytest.raises(SystemExit):
        parse_args()


# File Validation Tests (handled by CSVParser)
def test_validate_files_nonexistent_file(capsys):
    sys.argv = ["main.py", "nonexistent.csv"]
    with pytest.raises(SystemExit):
        driver_func()


def test_validate_files_invalid_extension(capsys):
    sys.argv = ["main.py", "tests/data/data1.txt"]
    with pytest.raises(SystemExit):
        driver_func()


# Main Function Tests
def test_main_with_valid_file(capsys):
    sys.argv = ["main.py", DATA1_PATH]
    driver_func()
    captured = capsys.readouterr()
    output = captured.out
    assert "Payout Report" in output
    assert "Department: Marketing" in output
    assert "Department: Design" in output
    assert "Alice Johnson" in output
    assert "Bob Smith" in output
    # 160, дезайн отдел: 150 + 170 = 320
    assert "160.00" in output
    assert "320.00" in output


def test_main_with_json_output(capsys):
    sys.argv = ["main.py", DATA1_PATH, DATA2_PATH, "--output", "json"]
    driver_func()
    captured = capsys.readouterr()
    output = captured.out
    assert output.startswith("{")
    assert '"Marketing"' in output
    assert '"Design"' in output
    assert '"HR"' in output
    assert '"Alice Johnson"' in output
    assert '"Grace Lee"' in output
    # 160 + 150 = 310
    # дизайн-  150 + 170 = 320
    # HR - 160 + 158 = 318
    assert '"total_hours": 310.0' in output
    assert '"total_hours": 320.0' in output
    assert '"total_hours": 318.0' in output


def test_main_with_nonexistent_file(capsys):
    sys.argv = ["main.py", "nonexistent.csv"]
    with pytest.raises(SystemExit):
        driver_func()


def test_main_with_invalid_extension(capsys):
    sys.argv = ["main.py", "tests/data/data1.txt"]
    with pytest.raises(SystemExit):
        driver_func()


def test_main_with_invalid_data(capsys):
    sys.argv = ["main.py", DATA3_PATH]
    driver_func()
    captured = capsys.readouterr()
    output = captured.out
    assert "Payout Report" in output
    assert "Department: Sales" in output
    assert "Department: HR" in output
    assert "Karen White" in output
    assert "Liam Harris" in output
    # 165 + 160 = 325, 155 для HR
    assert "325.00" in output
    assert "155.00" in output
