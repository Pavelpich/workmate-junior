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
        CSVParser("./employee_salary_report/tests/test_csv_reports/totaly_csv.txt")

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

def test_parser_normalize_headers():
    # Given
    parser_obj_1 = CSVParser("./csv_reports/data1.csv")
    parser_obj_2 = CSVParser("./csv_reports/data2.csv")
    parser_obj_3 = CSVParser("./csv_reports/data3.csv")

    assert parser_obj_1.headers == parser_obj_2.headers
    assert parser_obj_2.headers == parser_obj_3.headers


def test_parse_given_different_column_names_maps_correctly():
    # Given
    parser = CSVParser("./csv_reports/data2.csv")

    # When
    result = parser.parse()

    # Then
    assert "hourly_rate" in result[0]
    assert isinstance(result[0]["hourly_rate"], float)

def test_parse_given_missing_required_column_raises_value_error():
    # Given
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_missing_column.csv")
    
    # When & Then
    with pytest.raises(ValueError):
        parser.parse()

def test_parse_given_invalid_numeric_value_raises_value_error():
    # Given
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_invalid_data.csv")

    # When & Then
    with pytest.raises(ValueError):
        parser.parse()

def test_parse_given_empty_csv_returns_empty_list():

    # Given
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_empty.csv")
    
    # When
    result = parser.parse()

    # Then
    assert result == []
    assert parser.headers == ["id", "email", "name", "department", "hours_worked", "hourly_rate"]


def test_parse_given_different_column_order_returns_correct_data():
    # Given:
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_reordered.csv")

    # When
    result = parser.parse()

    # Then
    assert result[0] == {
        "id": 1,
        "email": "alice@example.com",
        "name": "Alice",
        "department": "Marketing",
        "hours_worked": 160,
        "hourly_rate": 50.0
    }

def test_parse_given_values_with_spaces_trims_correctly():
    # Given
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_spaces.csv")

    # When
    result = parser.parse()

    # Then
    assert result[0]["email"] == "alice@example.com"
    assert result[0]["name"] == "Alice"
    assert result[0]["department"] == "Marketing"

def test_parse_given_rate_column_maps_to_hourly_rate():
    # Given
    parser = CSVParser("./employee_salary_report/tests/test_csv_reports/test_rate.csv")

    # When
    result = parser.parse()

    # Then
    assert "hourly_rate" in result[0]
    assert result[0]["hourly_rate"] == 50.0
    assert "rate" not in result[0]