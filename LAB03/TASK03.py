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

class FullTimeStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__EssayName = kwargs.get('essay_name', "Trống")
        self.__EssayScore = kwargs.get('essay_score', 0.0)

class PartTimeStudent(Student):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__GraduationScore = kwargs.get('graduation_score', 0.0)