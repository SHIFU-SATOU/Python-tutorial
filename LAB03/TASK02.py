import re
import random
from abc import ABC, abstractmethod


class Staff(ABC):
    # Staff list
    __Staffs = []

    # Constructor
    def __init__(self, **kwargs):
        self._ID = kwargs.get('id')
        self._Name = kwargs.get('name', "Trống")
        money = float("".join(kwargs.get('salary').split("_")))
        self._Salary = money
        self._ResponsibilityIndex = kwargs.get('responsibility_index', 0.0)
        self._MonthlySalary = kwargs.get('monthly_salary', 0.0)

    # Print info of staff
    @abstractmethod
    def __str__(self) -> str:
        pass


class Expert(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__OvertimeHours = kwargs.get('overtime_hours', 0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Tăng ca: {self.__OvertimeHours}, Lương tháng: {self._MonthlySalary}"


class Researcher(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberInvention = kwargs.get('number_invention', 0)

    # Print info researcher
    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Phát minh: {self.__NumberInvention}, Lương tháng: {self._MonthlySalary}"


class Manager(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ConcurrentCoefficient = kwargs.get('concurrent_coefficient', 0.0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Kiêm nhiệm: {self.__ConcurrentCoefficient}, Lương tháng: {self._MonthlySalary}"

if __name__ == '__main__':
    StaffA = Expert(id=123, name="Nguyen A", salary='4_500_000', responsibility_index=0.5, overtime_hours=50)
    print(StaffA)
    StaffB = Researcher(id=124, name="Nguyen B", salary='5_600_000', responsibility_index=1.2, number_invention=10)
    print(StaffB)
    StaffC = Manager(id=125, name="Nguyen C", salary='7_800_800', responsibility_index=1.5, concurrent_coefficient=1.3)
    print(StaffC)