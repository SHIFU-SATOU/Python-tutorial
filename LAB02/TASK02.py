import math


class Coordinates:
    pass


class Coordinates:
    # Initialization method
    def __init__(self, latitude: int, longitude: int) -> None:
        self.__latitude = latitude
        self.__longitude = longitude

    # Instance method
    @property
    def latitude(self) -> int:
        return self.__latitude

    @latitude.setter
    def latitude(self, new_value: int) -> None:
        self.__latitude = new_value

    @property
    def longitude(self) -> int:
        return self.__longitude

    @longitude.setter
    def longitude(self, new_value: int) -> None:
        self.__latitude = new_value

    # Print coordinates
    def __str__(self) -> str:
        return f"x: {self.__latitude}, y: {self.__longitude}"

    # Move to coordinates
    def moveToDistance(self, distance: int) -> Coordinates:
        return Coordinates(self.__latitude + distance, self.__longitude + distance)

    # Caculate distance
    @classmethod
    def findDistance(cls, A: Coordinates, B: Coordinates) -> float:
        return round(math.sqrt((A.latitude - B.latitude) ** 2 + (A.longitude - B.longitude) ** 2), 3)

    # Find midpoint of 2 coordinates
    @classmethod
    def findMidpoint(cls, A: Coordinates, B: Coordinates) -> Coordinates:
        x_midpoint = (A.latitude + B.latitude) / 2
        y_midpoint = (A.longitude + B.longitude) / 2
        return Coordinates(x_midpoint, y_midpoint)

    # Reset coordinates
    def resetCoordinates(self) -> None:
        self.__latitude = 0
        self.__longitude = 0

    # Copy coordinates
    def copyCoordinates(self, other) -> None:
        self.__latitude = other.latitude
        self.__longitude = other.longitude

    @classmethod
    def findCoordinatesClosestToCenterO(cls, ListCordinates: list) -> Coordinates:
        O = Coordinates(0, 0)
        MinDistance = Coordinates.findDistance(O, ListCordinates[0])
        ClosestCoordinates = ListCordinates[0]
        for i in range(len(ListCordinates)):
            if Coordinates.findDistance(O, ListCordinates[i]) < MinDistance:
                MinDistance = Coordinates.findDistance(O, ListCordinates[i])
                ClosestCoordinates = ListCordinates[i]
        return ClosestCoordinates


if __name__ == '__main__':
    a = Coordinates(1, 1)
    b = Coordinates(2, 2)
    c = Coordinates(3, 3)
    d = Coordinates(4, 4)
    print(f"- Tọa độ A sau khi di chuyển thêm 4: {a.moveToDistance(4)}")
    print(f"- Khoảng cách giữa A và D là: {Coordinates.findDistance(a, d)}")
    print(f"- Trung điểm giữa B và D là: {Coordinates.findMidpoint(b, d)}")
    print(f"- Tọa độ điểm gần tâm O nhất: {Coordinates.findCoordinatesClosestToCenterO([a, b, c, d])}")
    a.resetCoordinates()
    print(f"- Tọa độ điểm A sau khi bị xóa: {a}")
    a.copyCoordinates(c)
    print(f"- Tọa độ điểm A sau khi sao chép tọa độ điểm c {c} là: {a}")
