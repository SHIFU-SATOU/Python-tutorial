from abc import ABC, abstractmethod
import math


class Point():
    pass


class Point(ABC):
    # Constructor
    def __init__(self, **kwargs):
        self.__X = kwargs.get('X', 0)
        self.__Y = kwargs.get('Y', 0)

    # Get X
    @property
    def X(self) -> int:
        return self.__X

    @property
    def Y(self) -> int:
        return self.__Y

    # Caculate distance of 2 points
    def caculateDistance(self, o_x: int, o_y: int) -> float:
        return round(math.sqrt((self.__X - o_x) ** 2 + (self.__Y - o_y) ** 2), 2)


class Circle():
    pass


class Circle(Point):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.__Radius = kwargs.get('Radius', 0)

    @property
    def Radius(self) -> float:
        return self.__Radius

    # Print info of circle
    def __str__(self) -> str:
        return f"Tâm O: ({self._Fraction__X}, {self._Fraction__Y})| Bán kính: {self.__Radius}"

    # Caculate perimeter
    def caculatePerimeter(self) -> float:
        return round(2 * math.pi * self.__Radius, 2)

    # Caculate square
    def caculateSquare(self) -> float:
        return round(math.pi * self.__Radius ** 2, 2)

    # Check if this circle intersects with another circle?
    def checkIntersects(self, other: Circle) -> bool:
        isTwoCirclesIntersectsion = False
        isTwoCirclesTouchInside = False
        Distance = self.caculateDistance(other.X, other.Y)
        if self.__Radius > other.Radius:
            isTwoCirclesIntersectsion = Distance > self.__Radius - other.Radius and Distance < self.__Radius + other.Radius
            isTwoCirclesTouchInside = Distance == self.__Radius - other.Radius
        elif self.__Radius < other.Radius:
            isTwoCirclesIntersectsion = Distance > other.Radius - self.__Radius and Distance < other.Radius - self.__Radius
            isTwoCirclesTouchInside = Distance == other.Radius - self.__Radius
        isTwoCirclesTouchOutside = Distance == self.__Radius + other.Radius
        return isTwoCirclesIntersectsion or isTwoCirclesTouchInside or isTwoCirclesTouchOutside


if __name__ == '__main__':
    A = Circle(X=4, Y=4, Radius=7)
    B = Circle(X=15, Y=4, Radius=4)
    # Print info of circle A
    print("-Thông tin đường tròn A:")
    print(A)
    # Caculate perimeter of circle A
    print(f"Chu vi đường tròn A: {A.caculatePerimeter()}")
    # Caculate square of circle A
    print(f"Diện tích đường tròn A: {A.caculateSquare()}")
    # Check circle A intersect to circle B
    print(f"Đường tròn A có giao đường tròn B không ? Kết quả: {A.checkIntersects(B)}")
