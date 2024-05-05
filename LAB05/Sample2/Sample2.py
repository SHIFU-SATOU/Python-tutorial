# Libaries
from abc import ABC, abstractmethod


class Ward:
    # Hàm khởi tạo phường
    def __init__(self, **kwargs) -> None:
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name')
        self.__HouseholdsList = []

    # Hàm thêm hộ vào phường
    def addHousehold(self, new_household) -> None:
        self.__HouseholdsList.append(new_household)

    # Hàm in danh sách các hộ
    def printHouseholdsList(self) -> None:
        temp = map(str, self.__HouseholdsList)
        print('\n'.join(temp))

    # Hàm tính tiền điện cho tất cả các hộ
    def caculateElectricBillForAllHouseholds(self) -> None:
        for e in self.__HouseholdsList:
            e.caculateElectricBill()

    # Hàm tính tiền điện trung bình của tất cả các hộ trong phường
    def caculateAverageElectricMoneyOfAllHouseholds(self) -> float:
        sum = 0.0
        for e in self.__HouseholdsList:
            sum += e.ElectricMoney
        return round(sum / len(self.__HouseholdsList), 2)

    # Hàm tìm những khách hàng có tiền điện lớn nhất
    def findRichestHouseholds(self) -> list:
        max = self.__HouseholdsList[0].ElectricMoney
        for e in self.__HouseholdsList:
            if e.ElectricMoney > max:
                max = e.ElectricMoney
        RichestHouseholds = []
        for e in self.__HouseholdsList:
            if e.ElectricMoney == max:
                RichestHouseholds.append(e)
        return RichestHouseholds

    # Hàm tìm những hộ sản xuất có tiền điện thấp nhất
    def findProductionHouseholdsWithLowestElectricMoney(self) -> list:
        min = self.__HouseholdsList[0].ElectricMoney
        for e in self.__HouseholdsList:
            if e.ElectricMoney < min:
                min = e.ElectricMoney
        Result = []
        for e in self.__HouseholdsList:
            if e.ElectricMoney == min:
                Result.append(e)
        return  Result


class absHousehold(ABC):
    # Hàm tính tiền điện
    @abstractmethod
    def caculateElectricBill(self) -> None:
        pass

    # Hàm xuất thông tin hộ
    @abstractmethod
    def __str__(self) -> str:
        pass


class Household(absHousehold):
    # Hàm khởi tạo hộ
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name')
        self.__OldIndex = int(kwargs.get('OldIndex'))
        self.__NewIndex = int(kwargs.get('NewIndex'))
        self.__ElectricMoney = 0.0

    @property
    def ElectricMoney(self) -> float:
        return self.__ElectricMoney

class Family(Household):
    def __str__(self) -> str:
        return f"ID: {self._Household__ID} || Tên: {self._Household__Name} || Chỉ số cũ: {self._Household__OldIndex} || Chỉ số mới: {self._Household__NewIndex} || Tiền điện: {self._Household__ElectricMoney}"

    # Hàm tính tiền điện của hộ gia đình
    def caculateElectricBill(self) -> None:
        A = self._Household__NewIndex - self._Household__OldIndex
        if A > 100:
            self._Household__ElectricMoney = A * 5500
        else:
            self._Household__ElectricMoney = A * 3500

class Business(Household):
    # Hàm khởi tạo hộ kinh doanh
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ElectricIndex = kwargs.get('ElectricIndex')

    def __str__(self) -> str:
        return f"ID: {self._Household__ID} || Tên: {self._Household__Name} || Chỉ số cũ: {self._Household__OldIndex} || Chỉ số mới: {self._Household__NewIndex} || Tiền điện: {self._Household__ElectricMoney}　|| Hệ số sử dụng: {self.__ElectricIndex}"

    # Hàm tính tiền điện của hộ kinh doanh
    def caculateElectricBill(self) -> None:
        A = self._Household__NewIndex - self._Household__OldIndex
        if A > 500:
            self._Household__ElectricMoney = A * 7000 * self.__ElectricIndex
        else:
            self._Household__ElectricMoney = A * 5500 * self.__ElectricIndex

class Production(Household):
    # Hàm khởi tạo hộ sản xuất
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ElectricIndex = kwargs.get('ElectricIndex')

    def __str__(self) -> str:
        return f"ID: {self._Household__ID} || Tên: {self._Household__Name} || Chỉ số cũ: {self._Household__OldIndex} || Chỉ số mới: {self._Household__NewIndex} || Tiền điện: {self._Household__ElectricMoney}　|| Hệ số sử dụng: {self.__ElectricIndex}"

    # Hàm tính tiền điện của hộ sản xuất
    def caculateElectricBill(self) -> None:
        A = self._Household__NewIndex - self._Household__OldIndex
        self._Household__ElectricMoney = A * 7000 * self.__ElectricIndex

if __name__ == '__main__':
    # TEST CASE
    # Khởi tạo nhanh 7 khách hàng
    H1 = Business(ID=123, Name='A', OldIndex=120, NewIndex=960, ElectricIndex=1.8)
    H2 = Family(ID=124, Name='B', OldIndex=400, NewIndex=450)
    H3 = Business(ID=125, Name='C', OldIndex=300, NewIndex=689, ElectricIndex=1.3)
    H4 = Production(ID=126, Name='D', OldIndex=150, NewIndex=965, ElectricIndex=1.5)
    H5 = Family(ID=127, Name='E', OldIndex=500, NewIndex=999)
    H6 = Production(ID=128, Name='F', OldIndex=350, NewIndex=987, ElectricIndex=1.6)
    H7 = Production(ID=129, Name='G', OldIndex=100, NewIndex=989, ElectricIndex=1.9)
    # Tạo phường A
    A = Ward(ID='P1', Name="Phường A")
    # Thêm 7 hộ gia đình vào phường
    A.addHousehold(H1)
    A.addHousehold(H2)
    A.addHousehold(H3)
    A.addHousehold(H4)
    A.addHousehold(H5)
    A.addHousehold(H6)
    A.addHousehold(H7)

    # Tính tiền điện cho tất cả các hộ
    A.caculateElectricBillForAllHouseholds()

    # In danh sách các hộ
    print("-Danh sách các hộ trong phường A:")
    A.printHouseholdsList()

    # Hàm tính tiền điện trung bình của tất cả các hộ trong phường
    print(f"-Tiền điện trung bình của phường: {A.caculateAverageElectricMoneyOfAllHouseholds()}")

    # Tìm những hộ có tiền điện cao nhất
    print("-Những hộ gia đình có tiền điện cao nhất:")
    print('\n'.join(map(str, A.findRichestHouseholds())))

    # Tìm những hộ sản xuất có tiền điện thấp nhất
    print("-Những hộ sản xuất có tiền điện thấp nhất:")
    print('\n'.join(map(str, A.findProductionHouseholdsWithLowestElectricMoney())))
