class Fraction:
    pass


class Fraction():
    # Constructor
    def __init__(self, numerator: int, denominator: int):
        self._Numerator = numerator
        self._Denominator = denominator

    # Get numerator
    @property
    def Numerator(self) -> int:
        return self._Numerator

    # Get Denominator
    @property
    def Denominator(self) -> int:
        return self._Denominator


class MixedNumber:
    pass

class MixedNumber(Fraction):
    def __init__(self, numerator: int, denominator: int, number: int):
        super().__init__(numerator, denominator)
        self.__Number = number

    # Print mixed number
    def __str__(self) -> str:
        return f"{self.__Number} {self._Numerator}/{self._Denominator}"

    # Convert fraction to mixed number
    # @staticmethod
    # def convertFractionToMixedNumber(fraction: Fraction) -> MixedNumber:
    #     IntergerNumber =