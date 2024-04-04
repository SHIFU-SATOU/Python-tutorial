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
        iNth = re.findall(r"[0-9]+", cls.__CurrentID)  # Get numbers of string
        iNextNth = int(iNth[0]) + 1  # Increased by 1
        # Append numbers to string
        if iNextNth in range(10):
            cls.__CurrentID = 'NV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__CurrentID = 'NV' + str(iNextNth)

    # Caculate monthly salary for all staffs
    @classmethod
    def caculateMonthlySalaryForAllStaffs(cls) -> None:
        for e in cls.__Staffs:
            e.caculateMonthlySalary()

    # Find staff by ID
    @classmethod
    def findStaffByID(cls, id: str) -> Staff:
        for e in cls.__Staffs:
            if e.ID == id:
                return e

    # Find staffs with lowest monthly salary
    @classmethod
    def findLaziestStaffs(cls) -> list:
        LaziestStaffs = []
        # Find lowest salary
        Min = 999999999
        for e in cls.__Staffs:
            if e.MonthlySalary < Min:
                Min = e.MonthlySalary

        # Find staff with monthly salary equal highest salary
        for e in cls.__Staffs:
            if e.MonthlySalary == Min:
                LaziestStaffs.append(e)

        return LaziestStaffs

    # Find sale staffs with highest monthly salary
    @classmethod
    def findBestSaleStaffs(cls) -> list:
        BestSaleStaffs = []
        # Find highest salary
        Max = 0
        for e in cls.__Staffs:
            if e.__name__ == "SaleStaff" and e.MonthlySalary > Max:
                Max = e.MonthlySalary
        # Find sale staffs with salary equal highest salary
        for e in cls.__Staffs:
            if e.__name__ == "SaleStaff" and e.MonthlySalary == Max:
                BestSaleStaffs.append(e)
        return BestSaleStaffs

    # Find top 10 staff with highest salary
    @classmethod
    def findTop10Staffs(cls) -> list:
        temp = cls.__Staffs.copy()
        Top10Staffs = []
        n = len(temp)
        # Rearrange the staffs list in ascending salary order
        for i in range(n):
            for j in range(0, n - i - 1):
                if temp[j].MonthlySalary < temp[j + 1].MonthlySalary:
                    temp[j], temp[j + 1] = temp[j + 1], temp[j]
        # Take first 10 staff
        return temp[:10]

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
