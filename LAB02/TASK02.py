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
