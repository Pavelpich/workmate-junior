class CSVParser:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.headers = []

    def parse(self) -> list[dict[str, str]]:
        with open(self.file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        self.headers = lines[0].strip().split(',')
        records = []
        for line in lines[1:]:
            values = line.strip().split(',')
            record = dict(zip(self.headers, values))
            records.append(record)
        return records