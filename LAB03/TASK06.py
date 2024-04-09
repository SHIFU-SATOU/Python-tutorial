import re
import random


class Student:
    pass


class Student:
    __Students = []
    __CurrentID = 'SV00'

    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Status = kwargs.get('Status', "Còn học")
        self.__GPA = kwargs.get('GPA', 0.0)

    # Get ID of student
    @property
    def ID(self) -> str:
        return self.__ID

    # Get status of student
    @property
    def Status(self) -> str:
        return self.__Status

    # Get GPA of student
    @property
    def GPA(self) -> float:
        return self.__GPA

    def __str__(self) -> str:
        return f"ID: {self.__ID} | Họ và tên: {self.__Name} | GPA: {self.__GPA} | Tình trạng: {self.__Status}"

    # Generate random students
    @classmethod
    def generateRandomStudents(cls, number_students: int) -> None:
        for i in range(number_students):
            Student.increaseID()
            id = cls.__CurrentID
            name = Student.__generateRandomName()
            gpa = Student.__generateRandomScore()
            status = Student.__generateRandomStatus()
            NewStudent = Student(ID=id, Name=name, Status=status, GPA=gpa)
            cls.__Students.append(NewStudent)

    # Print students list
    @classmethod
    def printStudents(cls) -> None:
        for e in cls.__Students:
            print(e)

    # Find student by ID
    @classmethod
    def findStudentByID(cls, id: str) -> Student:
        for e in cls.__Students:
            if e.ID == id:
                return e

    # Find students who drop out of school
    @classmethod
    def findStudentQuit(cls) -> list:
        QuitStudents = []
        for e in cls.__Students:
            if e.Status == "Thôi học":
                QuitStudents.append(e)
        return QuitStudents

    # Find students with highest GPA
    @classmethod
    def findBestStudents(cls) -> list:
        # Find highest GPA
        Max = cls.__Students[0].GPA
        for e in cls.__Students:
            if e.GPA > Max:
                Max = e.GPA
        # Find students with GPA equal highest GPA
        BestStudents = []
        for e in cls.__Students:
            if e.GPA == Max:
                BestStudents.append(e)
        return BestStudents

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

    # Generate random status
    @staticmethod
    def __generateRandomStatus() -> str:
        return random.choice(["Còn học", "Thôi học"])

class Class:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = str(kwargs.get('Name'), 'Trống')
        self.__Students = []
        self.__ClassNumber = kwargs.get('ClassNumber', 0)

    # Print info of school
    def __str__(self) -> str:
        return f"ID: {self.__ID} | Name: {self.__Name}"


if __name__ == '__main__':
    Student.generateRandomStudents(30)
    Student.printStudents()
    print("-Thông tin sinh viên SV19:")
    print(Student.findStudentByID('SV19'))
    print("-Danh sách sinh viên thôi học:")
    QuitStudents = Student.findStudentQuit()
    for e in QuitStudents:
        print(e)
    print("-Những sinh viên có điểm trung bình cao nhất:")
    BestStudents = Student.findBestStudents()
    for e in BestStudents:
        print(e)
