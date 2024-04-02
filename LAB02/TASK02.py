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
    def moveToCoordinates(self, distance: int) -> Coordinates:
        return Coordinates(self.__latitude + distance, self.__longitude + distance)

    # Caculate distance
    @classmethod
    def findDistance(cls, A: Coordinates, B: Coordinates) -> float:
        math.sqrt((A.latitude - B.latitude) ** 2 + (A.longitude - B.longitude) ** 2)


if __name__ == '__main__':
    print("Hello task 2")
