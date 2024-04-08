from abc import ABC, abstractmethod
import math


class Point(ABC):
    # Constructor
    def __init__(self, **kwargs):
        self._X = kwargs.get('X', 0)
        self._Y = kwargs.get('Y', 0)


class Circle(Point):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__Radius = kwargs.get('Radius', 0)

    # Print info of circle
    def __str__(self) -> str:
        return f"Tâm O: ({self._X}, {self._Y})| Bán kính: {self.__Radius}"

    # Caculate perimeter
    def caculatePerimeter(self) -> float:
        return round(2 * math.pi * self.__Radius, 2)

    # Caculate square
    def caculateSquare(self) -> float:
        return round(math.pi * self.__Radius ** 2, 2)
