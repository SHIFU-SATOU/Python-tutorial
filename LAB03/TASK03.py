import random
import re
from abc import ABC, abstractmethod

class Student(ABC):
    # Constructor
    def __init__(self, **kwargs):
        self._ID = str(kwargs.get('id'))
        self._Name = kwargs.get('name', "Trống")
        self._Address = kwargs.get('address', "Trống")
        self._NumberCredits = kwargs.get('number_credits', 0)
        self._GPA = kwargs.get('GPA', 0.0)
