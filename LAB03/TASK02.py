import re
import random
from abc import ABC, abstractmethod


class Staff(ABC):
    # Staff list
    __Staffs = []
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name', "Trống")
        self.__Salary = kwargs.get('salary', 0.0)
        self.__ResponsibilityIndex = kwargs.get('responsibility_index', 0.0)
        self.__MonthlySalary = kwargs.get('monthly_salary', 0.0)

