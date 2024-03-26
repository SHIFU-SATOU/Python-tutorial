class Staff:
    iNumberOfEmployees = 0

    def __init__(self, ID, Name, BaseSalary):
        self.ID = ID
        self.Name = Name
        self.BaseSalary = BaseSalary

        Staff.iNumberOfEmployees += 1

    def printInfo(self):
        print(f"+ Mã nhân viên: {self.ID}\n+Họ tên: {self.Name}\n+Lương cơ bản: {self.BaseSalary}")

    def __str__(self):
        return str(self.ID) + "_" + self.Name

    @classmethod
    def showNumberOfStagg(cls):
        return cls.iNumberOfEmployees
    @staticmethod
    def caculateStaffSalaryTotal(money):
        return money * 1.2


nv = Staff(123, "Nguyễn Văn A", 5000000)
print(nv)
print(f"Address variable: {hex(id(nv))}")

print(f"Số nhân viên đã tạo: {Staff.iNumberOfEmployees}")
print(f"Số nhân viên đã tạo: {Staff.showNumberOfStagg()}")