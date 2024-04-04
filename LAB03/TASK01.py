import math
import random
import re
from abc import ABC, abstractmethod


class Staff:
    pass


class Staff(ABC):
    __CurrentID = 'NV00'
    __Staffs = []

    # Constructor
    def __init__(self, **kwargs):
        self._ID = kwargs.get('id')
        self._Name = kwargs.get('name', 'Trống')
        self._Salary = kwargs.get('salary', 0.0)
        self._MonthlySalary = kwargs.get('monthly_salary', 0.0)

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

    # Print staffs list
    @classmethod
    def printStaffsList(cls) -> None:
        for e in cls.__Staffs:
            print(e)

    # Automatically create staff
    @classmethod
    def createRandomStaffs(cls, number: int) -> None:
        for i in range(number):
            Staff.increaseID()
            Name = Staff.__createRandomName()
            Salary = Staff.__createRandomSalary()
            TypeStaff = random.choice(['Sale', 'Office'])
            if TypeStaff == 'Sale':
                NumberProducts = SaleStaff.generateRandomNumberProducts()
                NewStaff = SaleStaff(id=cls.__CurrentID, name=Name, salary=Salary, number_products=NumberProducts)
                cls.__Staffs.append(NewStaff)
            elif TypeStaff == 'Office':
                NumberDay = OfficeStaff.generateRandomNumberWorkingDay()
                NewStaff = OfficeStaff(id=cls.__CurrentID, name=Name, salary=Salary, number_days=NumberDay)
                cls.__Staffs.append(NewStaff)

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


class SaleStaff:
    pass


class SaleStaff(Staff):

    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberProducts = kwargs.get('number_products', 0)

    # Print info of sale staff
    def __str__(self) -> str:
        return f"ID: {self._ID}, Họ và tên: {self._Name}, Lương cơ bản: {self._Salary}, Số sản phẩm: {self.__NumberProducts}, Lương hàng tháng: {self._MonthlySalary}"

    # Caculate monthly salary of sale staff
    def caculateMonthlySalary(self) -> None:
        NewMonthlySalary = self.__NumberProducts * 120000
        if NewMonthlySalary >= 8000000:
            NewMonthlySalary += NewMonthlySalary * 0.05
        elif NewMonthlySalary <= 5000000:
            NewMonthlySalary += NewMonthlySalary * 0.3
        self._MonthlySalary = round(NewMonthlySalary, 3)

    # Generate random number products
    @staticmethod
    def generateRandomNumberProducts() -> int:
        return random.randint(100, 200)


class OfficeStaff:
    pass


class OfficeStaff(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberWorkingDay = kwargs.get('number_days', 0)

    # print info of office staff
    def __str__(self) -> str:
        return f"ID: {self._ID}, Họ và tên: {self._Name}, Lương cơ bản: {self._Salary}, Số ngày làm việc: {self.__NumberWorkingDay}, Lương hàng tháng: {self._MonthlySalary}"

    # caculate monthly salary of office staff
    def caculateMonthlySalary(self) -> None:
        NewMonthlySalary = self.__NumberWorkingDay * 180000
        if NewMonthlySalary >= 8000000:
            NewMonthlySalary += NewMonthlySalary * 0.05
        self._MonthlySalary = round(NewMonthlySalary, 3)

    # Generate random number working day
    @staticmethod
    def generateRandomNumberWorkingDay() -> int:
        return random.randint(24, 26)


if __name__ == '__main__':
    Staff.createRandomStaffs(40)
    Staff.printStaffsList()
