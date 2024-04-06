import math
import re
import random
from abc import ABC, abstractmethod

class Staff(ABC):
    __Staffs = [] # staff list

    # Constructor
    def __init__(self, **kwargs) -> None:
        self.__ID = kwargs.get('ID')
        self.__Name = kwargs.get('Name', "Trống")
        self.__Salary = kwargs.get('Salary', 0.0)
        self.__ResponsibilityIndex = kwargs.get('ResponsibilityIndex', 0.0)
