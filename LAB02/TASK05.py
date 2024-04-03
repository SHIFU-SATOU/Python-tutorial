import math
import re
import random


class Staff:
    pass


class Staff:
    __CurrentID = 'NV00'
    __Staffs = []

    # Construtor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name', "Chưa bổ sung")
        self.__BaseSalary = kwargs.get('base salary', 0.0)
        self.__Products = kwargs.get('products', 0)
        self.__MonthlySalary = kwargs.get('monthly salary', 0.0)

    # Instance method
    @property
    def ID(self):
        return self.__ID

    # auto create id
    @classmethod
    def increaseID(cls):
        iNth = re.findall(r"[0-9]+", cls.__CurrentID)
        iNextNth = int(iNth[0]) + 1
        if iNextNth in range(10):
            cls.__CurrentID = 'NV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__CurrentID = 'NV' + str(iNextNth)

    # auto create name
    @staticmethod
    def __createRandomName() -> str:
        lLastNames = ['Nguyễn', 'Trần', 'Phạm', 'Hoàng', 'Bùi', 'Trịnh', 'Đặng', 'Vũ', 'Đồng']
        lFirstNames = ['Phú', 'Tân', 'Quân', 'Hậu', 'Lộc', 'Sơn', 'Khang', 'Quyên', 'Uyên', 'Tú', 'An', 'Bích', 'Duyên']
        lMiddleNames = ['', 'Thị', 'Chí', 'Minh', 'Đăng', 'Kim', 'Đức']
        return random.choice(lFirstNames) + ' ' + random.choice(lLastNames) + ' ' + random.choice(lMiddleNames)

    @staticmethod
    def __createRandomBaseSalary() -> float:
        return round(random.uniform(3000000, 5000000), 3)

    @staticmethod
    def __createRandomNumberProducts() -> int:
        return random.randint(100, 200)

    # print info of staff
    def __str__(self):
        return f"ID: {self.__ID}, Họ tên: {self.__Name}, Lương cơ bản: {self.__BaseSalary}, Số sản phẩm: {self.__Products}, Lương hàng tháng: {self.__MonthlySalary}"

    # caculate monthly salary for staff
    def caculateMonthlySalary(self) -> None:
        NewMoney = self.__BaseSalary + self.__Products * 175000
        if NewMoney >= 10000000:
            self.__MonthlySalary = NewMoney + NewMoney * 0.1
        else:
            self.__MonthlySalary = NewMoney

    # caculate monthly salary for all staffs
    @classmethod
    def caculateAllMonthlySalary(cls) -> None:
        for e in cls.__Staffs:
            e.caculateMonthlySalary()

    # create list staffs auto
    @classmethod
    def createStaffsAuto(cls, number: int) -> None:
        for i in range(number):
            Staff.increaseID()
            id = cls.__CurrentID
            name = Staff.__createRandomName()
            salary = Staff.__createRandomBaseSalary()
            products = Staff.__createRandomNumberProducts()
            NewStaff = Staff(id=id, name=name, salary=salary, products=products)
            cls.__Staffs.append(NewStaff)

    # print all staffs info
    @classmethod
    def printStaffsList(cls):
        for e in cls.__Staffs:
            print(e)

    # find staff by id
    @classmethod
    def findStaffByID(cls, id: str) -> Staff:
        for e in cls.__Staffs:
            if e.ID == id:
                return e


if __name__ == '__main__':
    Staff.createStaffsAuto(40)
    Staff.printStaffsList()
