import math

from TASK02 import Coordinates


class Circle:
    pass


class Circle:
    # constructor
    def __init__(self, r: int, x: int, y: int) -> None:
        self.__O = Coordinates(x, y)
        self.__r = r

    # instance method
    @property
    def O(self) -> Coordinates:
        return self.__O

    @property
    def r(self) -> int:
        return self.__r

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

    # Check if this circle intersects with another circle?
    def checkIntersects(self, other: Circle) -> bool:
        isTwoCirclesIntersectsion = False
        isTwoCirclesTouchInside = False
        Distance = Coordinates(self.__O, other.O)
        if self.__r > other.r:
            isTwoCirclesIntersectsion = Distance > self.__r - other.r and Distance < self.__r + other.r
            isTwoCirclesTouchInside = Distance == self.__r - other.r
        elif self.__r < other.r:
            isTwoCirclesIntersectsion = Distance > other.r - self.__r and Distance < other.r - self.__r
            isTwoCirclesTouchInside = Distance == other.r - self.__r
        isTwoCirclesTouchOutside = Distance == self.__r + other.r
        return isTwoCirclesIntersectsion or isTwoCirclesTouchInside or isTwoCirclesTouchOutside
