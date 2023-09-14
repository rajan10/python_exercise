"""
    Employee management system
"""


class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name = name
        self.salary = salary

    # def __repr__(self) -> str:
    #     return f"<Employee: {self.name}:{self.salary}>"

    def __str__(self) -> str:
        return f"<Employee: {self.name}:{self.salary}>"


class Manager(Employee):
    def __init__(self, name: str, salary: float, bonus: float) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_bonus(self):
        return self.salary * (self.bonus / 100)


class Developer(Employee):
    pass


manager1 = Manager(name="ram", salary=98456.23, bonus=10.0)
print(manager1)
