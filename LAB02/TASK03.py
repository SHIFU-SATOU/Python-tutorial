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
        if isRight and isIsosceles:
            return "tam giác vuông cân"
        elif isRight:
            return "tam giác vuông"
        elif isIsosceles:
            return "tam giác cân"
        elif isEquilateral:
            return "tam giác đều"
        else:
            return "tam giác bình thường"

    # caculate perimeter
    def caculatePerimeter(self) -> int:
        return self.__a + self.__b + self.__c

    # caculate square
    def caculateSquare(self) -> float:
        p = self.caculatePerimeter() / 2
        return round(math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c)), 3)

    # caculate radius of circumcircle of triangle
    def caculateRadiusOfCircumcircle(self) -> float:
        return round((self.__a * self.__b * self.__c) / (4 * self.caculateSquare()), 3)

    # caculate the radius of inscribed circle of triangle
    def caculateRadiusOfInscribedCircle(self) -> float:
        return round(2 * self.caculateSquare() / (self.__a + self.__b + self.__c), 3)


if __name__ == '__main__':
    a = Triangle(2, 2, 2 * 2 ** 0.5)

    print(f"-Độ dài ba cạnh lần lượt: {a}")
    print(f"-Loại tam giác: {a.findTypeOfTriangle()}")
    print(f"-Chu vi tam giác: {a.caculatePerimeter()}")
    print(f"-Diện tích tam giác: {a.caculateSquare()}")
    print(f"-Bán kính đường tròn ngoại tiếp: {a.caculateRadiusOfCircumcircle()}")
    print(f"-Bán kính đường tròn nội tiếp: {a.caculateRadiusOfInscribedCircle()}")
