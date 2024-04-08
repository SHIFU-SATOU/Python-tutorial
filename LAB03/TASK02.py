import re
import random
from abc import ABC, abstractmethod


class Staff(ABC):
    # Staff list
    __Staffs = []
    # Constructor
    def __init__(self, **kwargs):
        self._ID = kwargs.get('id')
        self._Name = kwargs.get('name', "Trống")
        self._Salary = kwargs.get('salary', 0.0)
        self._ResponsibilityIndex = kwargs.get('responsibility_index', 0.0)
        self._MonthlySalary = kwargs.get('monthly_salary', 0.0)

class Expert(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__OvertimeHours = kwargs.get('overtime_hours', 0)

class Researcher(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__NumberInvention = kwargs.get('number_invention', 0)

class Manager(Staff):
    # Constructor
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__ConcurrentCoefficient = kwargs.get('concurrent_coefficient', 0.0)
