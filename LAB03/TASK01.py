import math
import random
import re
from abc import ABC, abstractmethod


class Staff:
    pass


class Staff:
    __CurrentID = 'NV00'
    __Staffs = []

    # Constructor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name', 'Trống')
        self.__Salary = kwargs.get('salary', 0.0)
        self.__MonthlySalary = kwargs.get('monthly_salary', 0.0)

    # Instance methods
    # Get ID of staff
    @property
    def ID(self) -> str:
        return self.__ID

    # Get Name of staff
    @property
    def Name(self) -> str:
        return self.__Name

    # Get salary of staff
    @property
    def Salary(self) -> float:
        return self.__Salary

    # Get monthly salary of staff
    @property
    def MonthlySalary(self) -> float:
        return self.__MonthlySalary

    # Caculate monthly salary of staff
    @abstractmethod
    def caculateMonthlySalary(self) -> None:
        pass

    # Automatically generate ID
    @classmethod
    def increaseID(cls) -> None:
        iNth = re.findall(r"[0-9]+", cls.__CurrentID) #Get numbers of string
        iNextNth = int(iNth[0]) + 1 #Increased by 1
        #Append numbers to string
        if iNextNth in range(10):
            cls.__CurrentID = 'NV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__CurrentID = 'NV' + str(iNextNth)

        # Automatically create name
        @staticmethod
        def __createRandomName() -> str:
            lLastNames = ['Nguyễn', 'Trần', 'Phạm', 'Hoàng', 'Bùi', 'Trịnh', 'Đặng', 'Vũ', 'Đồng']
            lFirstNames = ['Phú', 'Tân', 'Quân', 'Hậu', 'Lộc', 'Sơn', 'Khang', 'Quyên', 'Uyên', 'Tú', 'An', 'Bích',
                           'Duyên']
            lMiddleNames = ['', 'Thị', 'Chí', 'Minh', 'Đăng', 'Kim', 'Đức']
            return random.choice(lFirstNames) + ' ' + random.choice(lLastNames) + ' ' + random.choice(lMiddleNames)

        # Automatically create salary
        @staticmethod
        def __createRandomSalary() -> float:
            return round(random.uniform(3000000, 5000000), 3)

