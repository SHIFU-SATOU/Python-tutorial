class Fraction:
    pass


class Fraction():
    # Constructor
    def __init__(self, numerator: int, denominator: int):
        self._Numerator = numerator
        self._Denominator = denominator

    # Print fraction
    def __str__(self):
        return f"{self._Numerator}/{self._Denominator}"

    # Get numerator
    @property
    def Numerator(self) -> int:
        return self._Numerator

    # Get Denominator
    @property
    def Denominator(self) -> int:
        return self._Denominator

    # Find greatest common divisor of fraction
    def findGCD(self) -> int:
        a = self._Numerator
        b = self._Denominator
        while b != 0:
            a, b = b, a % b
        return a

    # Shorten fraction
    def shortenFraction(self) -> Fraction:
        GCD = self.findGCD()
        return Fraction(self._Numerator // GCD, self._Denominator // GCD)


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
    @staticmethod
    def convertFractionToMixedNumber(fraction: Fraction) -> MixedNumber:
        IntergerPart = fraction.Numerator // fraction.Denominator
        NewNumerator = fraction.Numerator % fraction.Denominator
        NewDenominator = fraction.Denominator
        return MixedNumber(NewNumerator, NewDenominator, IntergerPart)

    # Convert mixed number to fraction
    def convertMixedNumberToFraction(self) -> Fraction:
        return Fraction(self.__Number * self._Denominator + self._Numerator, self._Denominator).shortenFraction()

if __name__ == "__main__":
    a = Fraction(5, 2)
    b = MixedNumber(1, 2, 2)
    # Convert fraction a to mixed number
    print(f"-Phân số a sau khi chuyển sang hỗn số: {MixedNumber.convertFractionToMixedNumber(a)}")
    # Convert mixed number b to fraction
    print(f"-Hỗn số b sau khi chuyển sang phân số: {b.convertMixedNumberToFraction()}")