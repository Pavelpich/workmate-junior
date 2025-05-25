class Employee:
    email: str
    name: str
    department: str
    hours_worked: int
    id: int
    hourly_rate: int
    salary: int

    def __init__(
        self,
        email: str,
        name: str,
        department: str,
        hours_worked: int,
        id: int,
        hourly_rate: int,
    ):

        if not name.strip():
            raise ValueError("Имя не может быть пустым")
        if not email.strip():
            raise ValueError("Email не может быть пустым")
        if not department.strip():
            raise ValueError("Департамент не может быть пустым")
        if hours_worked < 0:
            raise ValueError("Рабочие часы не могут быть отрицательными")
        if id < 0:
            raise ValueError("ID работника не может быть отрицательным")
        if hourly_rate < 0:
            raise ValueError("Почасовая ставка не может быть отрицательной")

        self.email = email
        self.name = name
        self.department = department
        self.hours_worked = hours_worked
        self.id = id
        self.hourly_rate = hourly_rate

    @property
    def salary(self) -> int:
        return self.hours_worked * self.hourly_rate
