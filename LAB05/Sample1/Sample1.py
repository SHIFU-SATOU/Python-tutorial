from abc import ABC, abstractmethod
class Company:
    # Hàm khởi tạo lớp công ty
    def __init__(self, **kwargs) -> None:
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', "Chưa đặt")
        self.__Staffs = []

    # Hàm thêm nhân viên
    def addStaff(self, staff) -> None:
        self.__Staffs.append(staff)

    # Hàm xuất danh sách nhân viên
    def printStaffsList(self) -> None:
        StaffsList = map(str, self.__Staffs)
        print('\n'.join(StaffsList))

    # Hàm tìm nhân viên theo mã nhân viên
    def findStaffByID(self, id: str):
        

class absStaff(ABC):
    # Hàm tính lương hàng tháng
    @abstractmethod
    def caculateMonthlySalary(self) -> None:
        pass
    # Hàm xuất thông tin nhân viên
    @abstractmethod
    def __str__(self) -> str:
        pass
    
class Staff(absStaff):
    def __init__(self, **kwargs) -> None:
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Salary = kwargs.get('Salary', 0.0)
        self.__MonthlySalary = 0
    
class OfficeStaff(Staff):
    # Hàm khởi tạo nhân viên văn phòng
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__TimeWork = kwargs.get('TimeWork', 0)
        self.__Subsidize = 0.0

    def caculateMonthlySalary(self) -> None:
        if(self.__TimeWork >= 100):
            self.__Subsidize = 5000000
        self._Staff__MonthlySalary = self._Staff__Salary + self.__TimeWork * 220000 + self.__Subsidize
        
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID} || Tên: {self._Staff__Name} || Lương cơ bản: {self._Staff__Salary} || Lương hàng tháng: {self._Staff__MonthlySalary} || Số giờ làm việc: {self.__TimeWork} || Trợ cấp: {self.__Subsidize}"
        
class ProductionStaff(Staff):
    # Hàm khởi tạo nhân viên sản xuất
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__ProductNumber = kwargs.get('ProductNumber', 0)
        
    def caculateMonthlySalary(self) -> None:
        Money = self._Staff__Salary + self.__ProductNumber * 175000
        if(self.__ProductNumber >= 150):
            self._Staff__MonthlySalary = Money + Money * 0.2
        else:
            self._Staff__MonthlySalary = Money
            
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID} || Tên: {self._Staff__Name} || Lương cơ bản: {self._Staff__Salary} || Lương hàng tháng: {self._Staff__MonthlySalary} || Số sản phẩm: {self.__ProductNumber}"
        
class Manager(Staff):
    # Hàm khởi tạo nhân viên quản lý
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.__PositionCoefficient = kwargs.get('PositionCoefficient', 0.0)
        self.__Reward = kwargs.get('Reward', 0.0)
        
    def caculateMonthlySalary(self) -> None:
        self._Staff__MonthlySalary = self._Staff__Salary * self.__PositionCoefficient + self.__Reward
    
    def __str__(self) -> str:
        return f"ID: {self._Staff__ID} || Tên: {self._Staff__Name} || Lương cơ bản: {self._Staff__Salary} || Lương hàng tháng: {self._Staff__MonthlySalary} || Hệ số chức vụ: {self.__PositionCoefficient} || Thưởng: {self.__Reward}"

if __name__ == '__main__':
    ComA = Company(ID=1, Name='A')
    
    O1 = OfficeStaff(ID=101, Name="Nguyễn A", Salary=4500000, TimeWork=200)
    ComA.addStaff(O1)
    O2 = OfficeStaff(ID=102, Name="Nguyễn B", Salary=5600000, TimeWork=100)
    ComA.addStaff(O2)
    O3 = OfficeStaff(ID=103, Name="Nguyễn C", Salary=8900000, TimeWork=90)
    ComA.addStaff(O3)
    
    P1 = ProductionStaff(ID=201, Name="Nguyễn D", Salary=7800000, ProductNumber=250)
    ComA.addStaff(P1)
    P2 = ProductionStaff(ID=202, Name="Nguyễn E", Salary=4500000, ProductNumber=110)
    ComA.addStaff(P2)
    P3 = ProductionStaff(ID=203, Name="Nguyễn F", Salary=6600000, ProductNumber=360)
    ComA.addStaff(P3)
    
    M1 = Manager(ID=301, Name="Nguyễn G", Salary=8500000, PositionCoefficient=1.3, Reward=19500000)
    ComA.addStaff(M1)
    M2 = Manager(ID=302, Name="Nguyễn H", Salary=7600000, PositionCoefficient=1.2, Reward=18600000)
    ComA.addStaff(M2)
    
    ComA.printStaffsList()