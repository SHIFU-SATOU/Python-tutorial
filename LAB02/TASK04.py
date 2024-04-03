import math


class Circle:
    # constructor
    def __init__(self, r: int) -> None:
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
