from .base_output import OutputFormatter

class ConsoleOutput(OutputFormatter):
    def render(self, data: dict) -> str:
        output = "Payout Report\n"
        for dept, details in data.items():
            output += f"\Department: {dept}\n"
            output += f"{'Employee':<15} {'Hours':>10} {'Hourly Rate':>16} {'Salary':>12}\n"
            output += "-" * 55 + "\n"
            for emp in details["employees"]:
                name = emp["name"]
                hours = f"{emp['hours']:.2f}"
                rate = f"{emp['hourly_rate']:.2f}"
                salary = f"{emp['salary']:.2f}"
                output += f"{name:<15} {hours:>10} {rate:>16} {salary:>12}\n"
            total_hours = f"{details['total_hours']:.2f}"
            total_salary = f"{details['total_salary']:.2f}"
            output += "-" * 55 + "\n"
            output += f"{'Total':<15} {total_hours:>10} {'':>16} {total_salary:>12}\n"
            
        return output