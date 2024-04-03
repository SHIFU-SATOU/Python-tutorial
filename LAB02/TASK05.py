import math
import re
import random


class Staff:
    __Flag = 'NV00'

    # Construtor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name', "Chưa bổ sung")
        self.__BaseSalary = kwargs.get('base salary', 0.0)
        self.__Products = kwargs.get('products', 0)
        self.__MonthlySalary = kwargs.get('monthly salary', 0.0)

    # auto create id
    @classmethod
    def createID(cls):
        iNth = re.findall(r"[0-9]+", cls.__Flag)
        iNextNth = int(iNth[0]) + 1
        if iNextNth in range(10):
            cls.__Flag = 'NV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__Flag = 'NV' + str(iNextNth)

    # auto create name
    @staticmethod
    def createRandomName(cls) -> str:
        lLastNames = ['Nguyễn', 'Trần', 'Phạm', 'Hoàng', 'Bùi', 'Trịnh', 'Đặng', 'Vũ', 'Đồng']
        lFirstNames = ['Phú', 'Tân', 'Quân', 'Hậu', 'Lộc', 'Sơn', 'Khang', 'Quyên', 'Uyên', 'Tú', 'An', 'Bích', 'Duyên']
        lMiddleNames = ['', 'Thị', 'Chí', 'Minh', 'Đăng', 'Kim', 'Đức']
        return random.choice(lFirstNames) + ' ' + random.choice(lLastNames) + ' ' + random.choice(lMiddleNames)

    @staticmethod
    def createRandomBaseSalary(cls) -> float:
        return round(random.uniform(3000000, 5000000), 3)

    @staticmethod
    def createRandomTypeStaff(cls) -> str:
        return random.choice(["Văn phòng", "Bán hàng"])

    @staticmethod
    def createRandomNumberDays() -> int:
        return random.randint(24, 26)

    @staticmethod
    def createRandomNumberProducts() -> int:
        return random.randint(100, 200)

