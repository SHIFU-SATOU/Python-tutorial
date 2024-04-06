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
