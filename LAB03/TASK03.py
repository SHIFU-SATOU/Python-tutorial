import random
import re
from abc import ABC, abstractmethod


class Student(ABC):
    __Students = []
    __CurrentID = 'SV00'

    # Constructor
    def __init__(self, **kwargs):
        self._ID = str(kwargs.get('id'))
        self._Name = kwargs.get('name', "Trống")
        self._Address = kwargs.get('address', "Trống")
        self._NumberCredits = kwargs.get('number_credits', 0)
        self._GPA = kwargs.get('gpa', 0.0)

    @abstractmethod
    def __str__(self) -> str:
        pass

    # Automatically create students
    @classmethod
    def createStudentsList(cls, number: int):
        Student.increaseID()
        name = Student.__generateRandomName()
        address = Student.__generateRandomAddress()
        number_credits = Student.__generateRandomNumberCredits()
        gpa = Student.__generateRandomScore()
        Type = ['Full-time', 'Part-time']
        for i in range(number):
            if random.choice(Type) == 'Full-time':
                essay_score = Student.__generateRandomScore()
                new_student = FullTimeStudent(id=cls.__CurrentID, name=name, address=address,
                                              number_credits=number_credits, gpa=gpa, essay_score=essay_score)
                cls.__Students.append(new_student)
            elif random.choice(Type) == 'Part-time':
                graduation_score = Student.__generateRandomScore()
                new_student = PartTimeStudent(id=cls.__CurrentID, name=name, address=address,
                                              number_credits=number_credits, gpa=gpa, graduation_score=graduation_score)
                cls.__Students.append(new_student)

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

    # Generate random address
    @staticmethod
    def __generateRandomAddress() -> str:
        HouseNumbers = str(random.randint(1, 1000))
        Streets = ["Võ Thị Sáu", "Điện Biên Phủ", "3 tháng 2", "Cách mạng tháng tám", "Nam kỳ khởi nghĩa",
                   "Phạm Văn Đồng", "30 tháng 4", "Huyền Trân công chúa", "Võ Nguyên Giáp", "Võ Văn Kiệt",
                   "Hoàng Hoa Thám", "Nguyễn Văn Trỗi", "Lê Văn Việt"]
        WardNumbers = str(random.randint(1, 10))
        Districts = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10",
                     "11", "Tân Bình", "Bình Tân", "Bình Thạnh", "Tân Phú"]
        return f"{HouseNumbers}/ {random.choice(Streets)}/ Phường {WardNumbers}/ Quận {random.choice(Districts)}"

    # Generate random number credits
    @staticmethod
    def __generateRandomNumberCredits() -> int:
        return random.randint(20, 160)

    # Generate random GPA
    @staticmethod
    def __generateRandomScore() -> float:
        return random.uniform(0, 10)


class FullTimeStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__EssayName = kwargs.get('essay_name', "Trống")
        self.__EssayScore = kwargs.get('essay_score', 0.0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Địa chỉ: {self._Address}, Tín chỉ: {self._NumberCredits}, GPA: {self._GPA}, Tên luận văn: {self.__EssayName}, Điểm luận văn: {self.__EssayScore}"

class PartTimeStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__GraduationScore = kwargs.get('graduation_score', 0.0)

    def __str__(self) -> str:
        return f"ID: {self._ID}, Tên: {self._Name}, Địa chỉ: {self._Address}, Tín chỉ: {self._NumberCredits}, GPA: {self._GPA}, Điểm thi tốt nghiệp: {self.__GraduationScore}"

if __name__ == '__main__':
    Student.createStudentsList(40)
