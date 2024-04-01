class Fraction:
    # Initialization method
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator

    @property
    def numerator(self) -> int:
        return self.__numerator

    @numerator.setter
    def numerator(self, new_value: int) -> None:
        self.__numerator = new_value

    @property
    def denominator(self) -> int:
        return self.__denominator

    @denominator.setter
    def denominator(self, new_value: int) -> None:
        self.__denominator = new_value

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"
