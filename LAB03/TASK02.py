import math
import re
import random
from abc import ABC, abstractmethod


class Staff(ABC):
    __Staffs = []  # staff list

    # Constructor
    def __init__(self, **kwargs) -> None:
        self.__ID = kwargs.get('ID')
        self.__Name = kwargs.get('Name', "Trống")
        self.__Salary = kwargs.get('Salary', 0.0)
        self.__ResponsibilityIndex = kwargs.get('ResponsibilityIndex', 0.0)
        self.__MonthlySalary = kwargs.get('MonthlySalary', 0.0)

    # Get ID of staff
    @property
    def ID(self) -> str:
        return self.__ID

    # Get salary of staff
    @property
    def Salary(self) -> float:
        return self.__Salary

    # Update salary of staff
    @Salary.setter
    def Salary(self, value: float) -> None:
        self.__Salary = value

    # Get responsibility index of staff
    @property
    def ResponsibilityIndex(self) -> float:
        return self.__ResponsibilityIndex

    # Get monthly salary
    def MonthlySalary(self) -> float:
        return self.__MonthlySalary

    # Print info of staff
    @abstractmethod
    def __str__(self) -> str:
        pass

    # Caculate monthly salary of staff
    @abstractmethod
    def caculateMonthlySalary(self) -> None:
        pass

    # Add staff
    @classmethod
    def addStaff(cls, staff) -> None:
        cls.__Staffs.append(staff)

    # Print staffs list
    @classmethod
    def printStaffsList(cls) -> None:
        for e in cls.__Staffs:
            print(e)

    # Caculate monthly salary for all staffs
    @classmethod
    def caculateMonthlySalaryForAllStaffs(cls) -> None:
        for e in cls.__Staffs:
            e.caculateMonthlySalary()

    # Find staff by ID
    @classmethod
    def findStaffByID(cls, id: str):
        for e in cls.__Staffs:
            if e.ID == id:
                return e

    # caculate labor costs
    @classmethod
    def caculateLaborCosts(cls) -> float:
        Money = 0.0
        for e in cls.__Staffs:
            Money += e.MonthlySalary
        return Money

    # Find ID of staff with largest monthly salary
    @classmethod
    def findIDOfBestStaff(cls) -> str:
        BestStaff = cls.__Staffs[0]
        for e in cls.__Staffs:
            if e.MonthlySalary > BestStaff.MonthlySalary:
                BestStaff = e
        return BestStaff.ID

    # Update salary of staff by ID
    @classmethod
    def updateSalaryOfStaff(cls, id: str, new_salary: float) -> None:
        for e in cls.__Staffs:
            if e.ID == id:
                e.Salary = new_salary
                break


class Expert(Staff):
    # Constructor
    def __init__(self, **kwargs) -> None:
        super().__init__()
        self.__OvertimeHours = kwargs.get('OvertimeHours', 0)

    def __str__(self) -> str:
        return f"ID: {self.__ID}, Họ và tên: {self.__Name}, Lương cơ bản: {self.__Salary}, Chỉ số trách nhiệm: {self.__ResponsibilityIndex}, Số giờ tăng ca: {self.__OvertimeHours}, Lương hàng tháng: {self.__MonthlySalary}"

    def caculateMonthlySalary(self) -> None:
        self.__MonthlySalary = self.__Salary + self.__Salary * self.__ResponsibilityIndex + self.__OvertimeHours * 180000
