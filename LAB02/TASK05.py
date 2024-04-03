import math
import re


class Staff:
    __Flag = 'NV00'

    # Construtor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name')
        self.__BaseSalary = kwargs.get('base salary')
        self.__Products = kwargs.get('products')
        self.__MonthlySalary = kwargs.get('monthly salary')

    @classmethod
    def createID(cls):
        iNth = re.findall(r"[0-9]+", cls.__Flag)
        iNextNth = int(iNth[0]) + 1
        if iNextNth in range(10):
            cls.__Flag = 'NV0' + str(iNextNth)
        elif (iNextNth > 9):
            cls.__Flag = 'NV' + str(iNextNth)

