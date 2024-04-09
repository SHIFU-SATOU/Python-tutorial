import re
import random


class Student:
    pass


class Student:

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

    # Generate random name
    @staticmethod
    def generateRandomName() -> str:
        lLastNames = ['Nguyễn', 'Trần', 'Phạm', 'Hoàng', 'Bùi', 'Trịnh', 'Đặng', 'Vũ', 'Đồng']
        lFirstNames = ['Phú', 'Tân', 'Quân', 'Hậu', 'Lộc', 'Sơn', 'Khang', 'Quyên', 'Uyên', 'Tú', 'An', 'Bích',
                       'Duyên']
        lMiddleNames = ['', ' Thị', ' Chí', ' Minh', ' Đăng', ' Kim', ' Đức']
        return random.choice(lFirstNames) + ' ' + random.choice(lLastNames) + random.choice(lMiddleNames)

    # Generate random GPA
    @staticmethod
    def generateRandomScore() -> float:
        return round(random.uniform(0, 10), 1)

    # Generate random status
    @staticmethod
    def generateRandomStatus() -> str:
        return random.choice(["Còn học", "Thôi học"])


class Class:

    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Students = []
        self.__StudentsNumber = 0

    # Print info of school
    def __str__(self) -> str:
        return f"ID: {self.__ID} | Tên: {self.__Name} | Sĩ số: {self.__StudentsNumber}"

    # Generate random students
    def generateRandomStudents(self, number_students: int) -> None:
        CurrentID = 'SV00'

        for i in range(number_students):
            # Automatically increase ID
            iNth = re.findall(r"[0-9]+", CurrentID)  # Get numbers of string
            iNextNth = int(iNth[0]) + 1  # Increased by 1
            # Append numbers to string
            if iNextNth in range(10):
                CurrentID = 'SV0' + str(iNextNth)
            elif (iNextNth > 9):
                CurrentID = 'SV' + str(iNextNth)

            id = CurrentID
            name = Student.generateRandomName()
            gpa = Student.generateRandomScore()
            status = Student.generateRandomStatus()
            NewStudent = Student(ID=id, Name=name, Status=status, GPA=gpa)
            self.__Students.append(NewStudent)
            self.__StudentsNumber += 1

    # Print students list
    def printStudents(self) -> None:
        for e in self.__Students:
            print(e)

    # Find student by ID
    def findStudentByID(self, id: str) -> Student:
        for e in self.__Students:
            if e.ID == id:
                return e

    # Find students who drop out of school
    def findStudentQuit(self) -> list:
        QuitStudents = []
        for e in self.__Students:
            if e.Status == "Thôi học":
                QuitStudents.append(e)
        return QuitStudents

    # Find students with highest GPA
    def findBestStudents(self) -> list:
        # Find highest GPA
        Max = self.__Students[0].GPA
        for e in self.__Students:
            if e.GPA > Max:
                Max = e.GPA
        # Find students with GPA equal highest GPA
        BestStudents = []
        for e in self.__Students:
            if e.GPA == Max:
                BestStudents.append(e)
        return BestStudents

class School:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__ClassesNumber = 0
        self.__Classes = []

    # Print info of school
    def __str__(self) -> str:
        return f"ID: {self.__ID} | Tên: {self.__Name} | Số lượng lớp học: {self.__ClassesNumber}"



if __name__ == '__main__':
    A = Class(ID=1, Name='A')
    A.generateRandomStudents(random.randint(30,50))
    print("-Thông tin lớp A")
    print(A)
    A.printStudents()
    print("-Thông tin sinh viên SV19:")
    print(A.findStudentByID('SV19'))
    print("-Danh sách sinh viên thôi học:")
    QuitStudents = A.findStudentQuit()
    for e in QuitStudents:
        print(e)
    print("-Những sinh viên có điểm trung bình cao nhất:")
    BestStudents = A.findBestStudents()
    for e in BestStudents:
        print(e)
