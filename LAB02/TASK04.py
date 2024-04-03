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
        return round(p + p * (percent / 100), 3)

    # zoom out circle by percent
    def zoomOutCircleByPercent(self, percent: int) -> float:
        p = self.caculatePerimeter()
        return round(p - p * (percent / 100), 3)

    # Check if this circle intersects with another circle?
    def checkIntersects(self, other: Circle) -> bool:
        isTwoCirclesIntersectsion = False
        isTwoCirclesTouchInside = False
        Distance = Coordinates.findDistance(self.__O, other.O)
        if self.__r > other.r:
            isTwoCirclesIntersectsion = Distance > self.__r - other.r and Distance < self.__r + other.r
            isTwoCirclesTouchInside = Distance == self.__r - other.r
        elif self.__r < other.r:
            isTwoCirclesIntersectsion = Distance > other.r - self.__r and Distance < other.r - self.__r
            isTwoCirclesTouchInside = Distance == other.r - self.__r
        isTwoCirclesTouchOutside = Distance == self.__r + other.r
        return isTwoCirclesIntersectsion or isTwoCirclesTouchInside or isTwoCirclesTouchOutside


if __name__ == "__main__":
    o = Circle(7, 4, 4)
    p = Circle(4, 15, 4)
    print(f"-Chu vi đường tròn o: {o.caculatePerimeter()}")
    print(f"-Diện tích đường tròn o: {o.caculateSquare()}")
    print(f"-Chu vi đường tròn o sau khi tăng 40%: {o.zoomInCircleByPercent(40)}")
    print(f"-Chu vi đường tròn o sau khi giảm 40%: {o.zoomOutCircleByPercent(40)}")
    print(f"-Kiểm tra đường tròn o có giao nhau với đường tròn p không ? Kết quả: {o.checkIntersects(p)}")
