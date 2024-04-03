import math

from TASK02 import Coordinates


class Circle:
    # constructor
    def __init__(self, r: int, x: int, y: int) -> None:
        self.__O = Coordinates(x, y)
        self.__r = r

    # print info of circle
    def __str__(self) -> str:
        return f"r = {self.__r}"

    # caculate perimeter
    def caculatePerimeter(self) -> float:
        return round(2 * math.pi * self.__r, 3)

    # caculate square
    def caculateSquare(self) -> float:
        return round(math.pi * self.__r ** 2, 3)

    # zoom in circle by percent
    def zoomInCircleByPercent(self, percent: int) -> float:
        p = self.caculatePerimeter()
        return p + p * (percent / 100)

    # zoom out circle by percent
    def zoomOutCircleByPercent(self, percent: int) -> float:
        p = self.caculatePerimeter()
        return p - p * (percent / 100)
