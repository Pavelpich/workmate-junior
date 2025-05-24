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
    def _cast_val(value: Any) -> str | int | float:
        value = value.strip()
        if value.isdigit():
            return int(value)

        try:
            return float(value)
        except ValueError:
            return value

    def parse(self) -> list[dict[str, str | int | float]]:
        with open(self.file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        parsed_headers = lines[0].strip().split(",")
        self.headers = [self.columns_mapping.get(it, it) for it in parsed_headers]

        records = []
        for line in lines[1:]:
            splitted_line = line.strip().split(",")
            values = [self._cast_val(it) for it in splitted_line]
            record = dict(zip(self.headers, values))
            records.append(record)
        return records
