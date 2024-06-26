import re
import random
from abc import ABC, abstractmethod


class Staff(ABC):
    # Staff list
    __Staffs = []

    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('id'))
        self.__Name = kwargs.get('name', "Trống")
        money = float("".join(kwargs.get('salary').split("_")))
        self.__Salary = money
        self.__ResponsibilityIndex = kwargs.get('responsibility_index', 0.0)
        self.__MonthlySalary = kwargs.get('monthly_salary', 0.0)

    # Get ID of staff
    @property
    def ID(self) -> str:
        return self.__ID

    # Get monthly salary of staff
    @property
    def MonthlySalary(self) -> float:
        return self.__MonthlySalary

    # Get salary of staff
    @property
    def Salary(self) -> float:
        return self.__Salary

    # Set salary of staff
    @Salary.setter
    def Salary(self, money: float) -> None:
        self.__Salary = money

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
        # map(lambda staff: print(staff), cls.__Staffs)

    # Caculate monthly salary for all staffs
    @classmethod
    def caculateAllMonthlySalary(cls) -> None:
        for e in cls.__Staffs:
            e.caculateMonthlySalary()

    # Find staff by ID
    @classmethod
    def findStaffByID(cls, id: str):
        for e in cls.__Staffs:
            if e.ID == id:
                return e

    # Caculate labors cost
    @classmethod
    def caculateLaborsCost(cls) -> float:
        Total = 0
        for e in cls.__Staffs:
            Total += e.MonthlySalary
        return round(Total, 2)

    # Find staffs with highest monthly salary
    @classmethod
    def findBestStaffs(cls) -> list:
        # Find highest salary
        Max = 0
        for e in cls.__Staffs:
            if e.MonthlySalary > Max:
                Max = e.MonthlySalary
        # Find staffs with salary equal highest salary
        BestStaffs = []
        for e in cls.__Staffs:
            if e.MonthlySalary == Max:
                BestStaffs.append(e.ID)
        return BestStaffs

    # Update salary by ID
    @classmethod
    def updateSalaryByID(cls, id: str, money: float) -> None:
        for e in cls.__Staffs:
            if e.ID == id:
                e.Salary = money


class Expert(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__OvertimeHours = kwargs.get('overtime_hours', 0)

    def __str__(self) -> str:
        return f"ID: {self._Staff__ID}, Tên: {self._Staff__Name}, Lương: {self._Staff__Salary}, Trách nhiệm: {self._Staff__ResponsibilityIndex}, Tăng ca: {self.__OvertimeHours}, Lương tháng: {self._Staff__MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._Staff__MonthlySalary = self._Staff__Salary + self._Staff__Salary * self._Staff__ResponsibilityIndex + self.__OvertimeHours * 180000


class Researcher(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberInvention = kwargs.get('number_invention', 0)

    # Print info researcher
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID}, Tên: {self._Staff__Name}, Lương: {self._Staff__Salary}, Trách nhiệm: {self._Staff__ResponsibilityIndex}, Phát minh: {self.__NumberInvention}, Lương tháng: {self._Staff__MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._Staff__MonthlySalary = self._Staff__Salary + self._Staff__Salary * (
                self._Staff__ResponsibilityIndex - 0.2) + self.__NumberInvention * 5500000


class Manager(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ConcurrentCoefficient = kwargs.get('concurrent_coefficient', 0.0)

    def __str__(self) -> str:
        return f"ID: {self._Staff__ID}, Tên: {self._Staff__Name}, Lương: {self._Staff__Salary}, Trách nhiệm: {self._Staff__ResponsibilityIndex}, Kiêm nhiệm: {self.__ConcurrentCoefficient}, Lương tháng: {self._Staff__MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self._Staff__MonthlySalary = self._Staff__Salary * 0.7 + self._Staff__Salary * self._Staff__ResponsibilityIndex + self._Staff__Salary * self.__ConcurrentCoefficient


if __name__ == '__main__':
    StaffA = Expert(id=123, name="Nguyen A", salary='4_500_000', responsibility_index=0.5, overtime_hours=50)
    Staff.addStaff(StaffA)
    StaffB = Researcher(id=124, name="Nguyen B", salary='5_600_000', responsibility_index=1.2, number_invention=10)
    Staff.addStaff(StaffB)
    StaffC = Manager(id=125, name="Nguyen C", salary='7_800_800', responsibility_index=1.5, concurrent_coefficient=1.3)
    Staff.addStaff(StaffC)
    StaffD = Researcher(id=126, name="Nguyen D", salary='8_100_000', responsibility_index=0.8, number_invention=12)
    Staff.addStaff(StaffD)
    StaffE = Manager(id=127, name="Nguyen E", salary='9_500_000', responsibility_index=1.0, concurrent_coefficient=1.6)
    Staff.addStaff(StaffE)
    StaffF = Expert(id=128, name="Nguyen F", salary='6_500_000', responsibility_index=0.8, overtime_hours=30)
    Staff.addStaff(StaffF)

    # Caculate monthly salary for all staff
    Staff.caculateAllMonthlySalary()
    # Print staffs list
    print("-Danh sách nhân viên:")
    Staff.printStaffsList()
    # Find staff with ID: 125
    print("-Nhân viên ID:125")
    print(Staff.findStaffByID('125'))
    # Caculate labors cost
    print(f"-Chi phí nhân công: {Staff.caculateLaborsCost()}")
    # Find staffs with highest monthly salary
    print("-Những nhân viên có lương cao nhất:")
    BestStaffs = Staff.findBestStaffs()
    for e in BestStaffs:
        print(e)
    # Update salary of staff with ID: 125
    print("-Lương mới của nhân viên 125 sau khi được cập nhật lương:")
    Staff.updateSalaryByID('125', 1000000)
    print(Staff.findStaffByID('125'))
