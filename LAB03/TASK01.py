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
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name', 'Trống')
        self.__Salary = kwargs.get('salary', 0.0)
        self.__MonthlySalary = kwargs.get('monthly_salary', 0.0)
        self.__Type = 'Trống'

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
        map(lambda e: e.caculateMonthlySalary(), cls.__Staffs)

    # Find staff by ID
    @classmethod
    def findStaffByID(cls, id: str):
        return filter(lambda e: e.ID == id, cls.__Staffs)

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
        LaziestStaffs.extend(filter(lambda e: e.MonthlySalary == Min, cls.__Staffs))

        return LaziestStaffs

    # Find sale staffs with highest monthly salary
    @classmethod
    def findBestSaleStaffs(cls) -> list:
        BestSaleStaffs = []
        # Find highest salary
        Max = 0
        for e in cls.__Staffs:
            if e.__class__.__name__ == "SaleStaff" and e.MonthlySalary > Max:
                Max = e.MonthlySalary
        # Find sale staffs with salary equal highest salary
        BestSaleStaffs.extend(
            filter(lambda e: e.__class__.__name__ == "SaleStaff" and e.MonthlySalary == Max, cls.__Staffs))
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
        map(lambda e: print(e), cls.__Staffs)

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
        self._Staff__Type = "Kinh doanh"
        self.__NumberProducts = kwargs.get('number_products', 0)

    # Print info of sale staff
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID}, Họ và tên: {self._Staff__Name}, Lương cơ bản: {self._Staff__Salary}, Số sản phẩm: {self.__NumberProducts}, Lương hàng tháng: {self._Staff__MonthlySalary}, Loại: {self._Staff__Type}"

    # Caculate monthly salary of sale staff
    def caculateMonthlySalary(self) -> None:
        NewMonthlySalary = self.__NumberProducts * 120000
        if NewMonthlySalary >= 8000000:
            NewMonthlySalary += NewMonthlySalary * 0.05
        elif NewMonthlySalary <= 5000000:
            NewMonthlySalary += NewMonthlySalary * 0.3
        self._Staff__MonthlySalary = round(NewMonthlySalary, 3)

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
        self._Staff__Type = "Văn phòng"
        self.__NumberWorkingDay = kwargs.get('number_days', 0)

    # print info of office staff
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID}, Họ và tên: {self._Staff__Name}, Lương cơ bản: {self._Staff__Salary}, Số ngày làm việc: {self.__NumberWorkingDay}, Lương hàng tháng: {self._Staff__MonthlySalary}, Loại: {self._Staff__Type}"

    # caculate monthly salary of office staff
    def caculateMonthlySalary(self) -> None:
        NewMonthlySalary = self.__NumberWorkingDay * 180000
        if NewMonthlySalary >= 8000000:
            NewMonthlySalary += NewMonthlySalary * 0.05
        self._Staff__MonthlySalary = round(NewMonthlySalary, 3)

    # Generate random number working day
    @staticmethod
    def generateRandomNumberWorkingDay() -> int:
        return random.randint(24, 26)


if __name__ == '__main__':
    # Automatically create 40 staffs
    Staff.createRandomStaffs(40)
    # Update monthly salary for all staffs
    Staff.caculateMonthlySalaryForAllStaffs()
    # Print staffs list
    Staff.printStaffsList()
    # Find staff with ID = NV19
    print("-Thông tin nhân viên có mã số NV19:")
    print(Staff.findStaffByID('NV19'))
    # Find laziest staffs
    print("-Những nhân viên có lương thấp nhất:")
    LaziestStaffs = Staff.findLaziestStaffs()
    for e in LaziestStaffs:
        print(e)
    # Find best sale staffs
    print("-Những nhân viên bán hàng có lương cao nhất:")
    BestSaleStaffs = Staff.findBestSaleStaffs()
    for e in BestSaleStaffs:
        print(e)

    # Find top 10 staffs
    print("-Top 10 nhân viên có lương cao nhất:")
    Top10Staffs = Staff.findTop10Staffs()
    for e in Top10Staffs:
        print(e)
