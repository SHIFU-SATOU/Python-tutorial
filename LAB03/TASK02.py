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

    # Get ID of staff
    @property
    def ID(self) -> str:
        return self._ID

    # Get monthly salary of staff
    @property
    def salary(self) -> float:
        return self._Salary

    # Print info of staff
    @abstractmethod
    def __str__(self) -> str:
        pass

    # Caculate monthly salary
    @abstractmethod
    def caculateMonthlySalary(self) -> None:
        pass

    # Add staff to staffs list
    @classmethod
    def addStaff(cls, staff) -> None:
        cls.__Staffs.append(staff)

    # Print staffs list
    @classmethod
    def printStaffsList(cls) -> None:
        for e in cls.__Staffs:
            print(e)


class Expert(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__OvertimeHours = kwargs.get('overtime_hours', 0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Tăng ca: {self.__OvertimeHours}, Lương tháng: {self._MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._MonthlySalary = self._Salary + self._Salary * self._ResponsibilityIndex + self.__OvertimeHours * 180000


class Researcher(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberInvention = kwargs.get('number_invention', 0)

    # Print info researcher
    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Phát minh: {self.__NumberInvention}, Lương tháng: {self._MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._MonthlySalary = self._Salary + self._Salary * (
                self._ResponsibilityIndex - 0.2) + self.__NumberInvention * 5500000


class Manager(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ConcurrentCoefficient = kwargs.get('concurrent_coefficient', 0.0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Lương: {self._Salary}, Trách nhiệm: {self._ResponsibilityIndex}, Kiêm nhiệm: {self.__ConcurrentCoefficient}, Lương tháng: {self._MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._MonthlySalary = self._Salary * 0.7 + self._Salary * self._ResponsibilityIndex + self._Salary * self.__ConcurrentCoefficient


if __name__ == '__main__':
    StaffA = Expert(id=123, name="Nguyen A", salary='4_500_000', responsibility_index=0.5, overtime_hours=50)
    StaffA.caculateMonthlySalary()
    Staff.addStaff(StaffA)
    StaffB = Researcher(id=124, name="Nguyen B", salary='5_600_000', responsibility_index=1.2, number_invention=10)
    StaffB.caculateMonthlySalary()
    Staff.addStaff(StaffB)
    StaffC = Manager(id=125, name="Nguyen C", salary='7_800_800', responsibility_index=1.5, concurrent_coefficient=1.3)
    StaffC.caculateMonthlySalary()
    Staff.addStaff(StaffC)
    Staff.printStaffsList()
