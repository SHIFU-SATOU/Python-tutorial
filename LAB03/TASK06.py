import re
import random

class Student:
    __Students = []
    __CurrentID = 'SV00'

    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Status = kwargs.get('Status', "Còn học")

    # Automatically generate ID
    @classmethod
    def increaseID(cls) -> None:
        iNth = re.findall(r"[0-9]+", cls.__CurrentID)  # Get numbers of string
        iNextNth = int(iNth[0]) + 1  # Increased by 1
        # Append numbers to string
        if iNextNth in range(10):
            cls.__CurrentID = 'SV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__CurrentID = 'SV' + str(iNextNth)

    # Generate random name
    @staticmethod
    def __generateRandomName() -> str:
        lLastNames = ['Nguyễn', 'Trần', 'Phạm', 'Hoàng', 'Bùi', 'Trịnh', 'Đặng', 'Vũ', 'Đồng']
        lFirstNames = ['Phú', 'Tân', 'Quân', 'Hậu', 'Lộc', 'Sơn', 'Khang', 'Quyên', 'Uyên', 'Tú', 'An', 'Bích',
                       'Duyên']
        lMiddleNames = ['', ' Thị', ' Chí', ' Minh', ' Đăng', ' Kim', ' Đức']
        return random.choice(lFirstNames) + ' ' + random.choice(lLastNames) + random.choice(lMiddleNames)

    # Generate random GPA
    @staticmethod
    def __generateRandomScore() -> float:
        return round(random.uniform(0, 10), 1)