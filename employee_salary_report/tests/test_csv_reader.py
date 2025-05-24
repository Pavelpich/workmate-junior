import pytest
from employee_salary_report.parsers.csv_parser import CSVParser

def test_parse_given_empty_path_raises_file_not_found():
    # Given & When & Then
    with pytest.raises(FileNotFoundError):
        CSVParser("")

def test_parse_given_invalid_path_raises_file_not_found():
    # Given & When & Then
    with pytest.raises(FileNotFoundError):
        CSVParser("./csv_reports/data_sata12.csv")

def test_parse_given_non_csv_extension_raises_error():
    # Given & When & Then
    with pytest.raises(TypeError):
        CSVParser("./csv_reports/totaly_csv.txt")

def test_parser_work_returns_valid_outcome():
    # Given
    parser_obj = CSVParser("./csv_reports/data1.csv")

    # When
    res = parser_obj.parse()

    # Then
    assert res[0]["email"] == "alice@example.com"
    assert res[0]["name"] == "Alice Johnson"
    assert res[0]["department"] == "Marketing"
    assert res[0]["hours_worked"] == 160
    assert res[0]["id"] == 1
    assert res[0]["hourly_rate"] == 50

    assert res[2]["email"] == "carol@example.com"
    assert res[2]["name"] == "Carol Williams"
    assert res[2]["department"] == "Design"
    assert res[2]["hours_worked"] == 170
    assert res[2]["id"] == 3
    assert res[2]["hourly_rate"] == 60

def test_csvparser_work_validity():
    # Given
    parser_obj_1 = CSVParser("./csv_reports/data1.csv")
    parser_obj_2 = CSVParser("./csv_reports/data2.csv")
    parser_obj_3 = CSVParser("./csv_reports/data3.csv")

    assert parser_obj_1.headers == parser_obj_2.headers
    assert parser_obj_2.headers == parser_obj_3.headers