import math


class Triangle:
    pass


class Triangle:

    # Constructor
    def __init__(self, a, b, c) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    # print triangle
    def __str__(self) -> str:
        return f"{self.__a}, {self.__b}, {self.__c}"

    # find type of triangle
    def findTypeOfTriangle(self) -> str:
        isRight = (self.__a ** 2 + self.__b ** 2 == self.__c ** 2 or self.__b ** 2 + self.__c ** 2 == self.__a ** 2 or
                   self.__c ** 2 + self.__a ** 2 == self.__b ** 2)
        isIsosceles = self.__a == self.__b or self.__b == self.__c or self.__c == self.__a
        isEquilateral = self.__a == self.__b and self.__b == self.__c
        if isRight:
            if isIsosceles:
                return "Tam giác vuông cân"
            else:
                return "Tam giác vuông"
        elif isIsosceles:
            return "Tam giác cân"
        elif isEquilateral:
            return "Tam giác đều"
        else:
            return "Tam giác bình thường"

    # caculate perimeter
    def caculatePerimeter(self) -> int:
        return self.__a + self.__b + self.__c

    # caculate square
    def caculateSquare(self) -> float:
        p = self.caculatePerimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))
