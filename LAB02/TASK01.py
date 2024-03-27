class Fraction:
    # Data components
    def __init__(self, **kwargs):
        self.__Numerator = int(kwargs.get('Tử số'))
        self.__Denominator = int(kwargs.get('Mẫu số'))

    # Processing ingredients
    @property
    def Numerator(self) -> int:
        return self.__Numerator

    @Numerator.setter
    def Numerator(self, iNewValue: int) -> None:
        self.__Numerator = iNewValue

    @property
    def Denominator(self) -> int:
        return self.__Denominator

    @Denominator.setter
    def Denominator(self, iNewValue: int) -> None:
        self.__Denominator = iNewValue

    # Finding greatest common divisor
    @staticmethod
    def __findGCD(iA: int, iB: int) -> int:
        while iB != 0:
            iA, iB = iB, iA % iB
        return iA

    # Shortening fraction
    def __shortenFraction(self):
        iGCD = self.__findGCD(self.Numerator, self.Denominator)
        iNewNumerator = self.__Numerator // iGCD
        iNewDenominator = self.__Denominator // iGCD
        return Fraction(iNewNumerator, iNewDenominator)

    # Redefine the output method
    def __str__(self):
        return f"{self.__Numerator}/{self.__Denominator}"

    # Adding 2 fractions
    def __add__(self, other):
        iNewNumerator = 0
        iNewDenominator = 0
        if(type(other)==type(int())):
            iNewNumerator = self.__Numerator + other * self.__Denominator
            return Fraction(iNewNumerator, self.__Denominator).__shortenFraction()
        else:
            iNewNumerator = self.__Numerator * other.Denominator + other.Numerator * self.__Denominator
            iNewDenominator = self.__Denominator * other.Denominator
            return Fraction(iNewNumerator, iNewDenominator).__shortenFraction()


    # Subtracting 2 fractions
    def __sub__(self, other):
        iNewNumerator = self.__Numerator * other.__Denominator - other.Numerator * self.__Denominator
        iNewDenominator = self.__Denominator * other.__Denominator
        return Fraction(iNewNumerator, iNewDenominator).__shortenFraction()
