#Libaries
from abc import ABC, abstractmethod

class absHousehold(ABC):
    # Hàm tính tiền điện
    @abstractmethod
    def caculateElectricBill(self) -> None:
        pass

class Household(absHousehold):
    # Hàm khởi tạo hộ
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name')
        self.__OldIndex = kwargs.get('OldIndex')
        self.__NewIndex = kwargs.get('NewIndex')
        
    # Hàm xuất thông tin hộ
    def __str__(self) -> str:
        return f"ID: {self.__ID} || Tên: {self.__Name} || Chỉ số cũ: {self.__OldIndex} || Chỉ số mới: {self.__NewIndex}"
        
class Family(Household):
    pass

class Business(Household):
    # Hàm khởi tạo hộ kinh doanh
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ElectricIndex = kwargs.get('ElectricIndex')

class Production(Household):
    # Hàm khởi tạo hộ sản xuất
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ElectricIndex = kwargs.get('ElectricIndex')
