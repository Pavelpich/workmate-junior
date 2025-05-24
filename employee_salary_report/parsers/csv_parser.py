from os.path import exists
from typing import Any


class CSVParser:
    columns_mapping = {
        'salary':'hourly_rate',
        'rate':'hourly_rate',
        'department':'department',
        'id':'id',
        'email':'email',
        'name':'name',
        'hour_worked':'hours_worked'
    }

    def __init__(self, file_path: str):
        if not exists(file_path):
            raise FileNotFoundError(f"Передан некорректный путь к файлу: '{file_path}'")

        if file_path.split(".")[-1] != "csv":
            raise TypeError(
                f"Файл {file_path} переданный в парсер не является файлом .csv"
            )

        self.file_path = file_path
        self.headers = []

    @staticmethod
    def _cast_val(value: str, field_name: str) -> str | int | float:
        value = value.strip()
        if field_name == "id":
            if not value.isdigit():
                raise ValueError(f"Передано неверное значение для поля id: {value}")
            return int(value)
        elif field_name in ["hours_worked", "hourly_rate"]:
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"Передано неверное значение для поля {field_name}: {value}")
        else:
            return value

    def parse(self) -> list[dict[str, str | int | float]]:
        required_columns = {"id", "email", "name", "department", "hours_worked", "hourly_rate"}
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        parsed_headers = lines[0].strip().split(",")
        self.headers = [self.columns_mapping.get(it, it) for it in parsed_headers]

        # Проверяем, что все обязательные колонки есть в header
        if not required_columns.issubset(self.headers):
            missing = required_columns - set(self.headers)
            raise ValueError(f"В файле {self.file_path} не хватает обязательных колонок в header: {missing}")

        records = []
        for line in lines[1:]:
            split_values = line.strip().split(",")
            if len(split_values) != len(self.headers):
                raise ValueError(f"Строка содержит {len(split_values)} колонок, ожидалось {len(self.headers)}")
            values = [self._cast_val(val, field) for val, field in zip(split_values, self.headers)]
            record = dict(zip(self.headers, values))
            records.append(record)
        return records
