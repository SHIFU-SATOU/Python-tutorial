# Task 01: Building fraction class
from fractions import Fraction


class Fraction:
    # Data components
    def __init__(self, iNumerator: int, iDenominator: int):
        self.__Numerator = iNumerator
        self.__Denominator = iDenominator

    # Processing ingredients
    @property
    def Numerator(self):
        return self.__Numerator

    @property
    def Denominator(self):
        return self.__Denominator

    @Numerator.setter
    def Numerator(self, iNewValue: int):
        self.__Numerator = iNewValue

    @Denominator.setter
    def Denominator(self, iNewValue: int):
        self.__Denominator = iNewValue

    @staticmethod
    def findGCD(iA: int, iB: int) -> int:
        while iB:
            iA, iB = iB, iA % iB
        return iA

    # 4. Shorten fraction
    def shortenFraction(self):
        Result = Fraction(0, 1)
        GCD = self.findGCD(self.Numerator, self.Denominator)
        Result.Numerator = self.Numerator // GCD
        Result.Denominator = self.Denominator // GCD
        return Result

    # 10. Finding largest fraction
    @staticmethod
    def findLargestFraction(Fractions: list) -> Fraction:
        Max = Fractions[0]
        for i in range(len(Fractions)):
            if Fractions[i] > Max:
                Max = Fractions[i]
        return Max

    # 2. Print fraction
    def __str__(self):
        return f"{self.Numerator}/{self.Denominator}"

    def __add__(self, other):
        ResultNumerator = 0
        ResultDenominator = 0
        if (type(other) == type(int())):
            ResultNumerator = self.Numerator + other * self.Denominator
            ResultDenominator = self.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()
        else:
            ResultNumerator = self.Numerator * other.Denominator + other.Numerator * self.Denominator
            ResultDenominator = self.Denominator * other.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()

    def __sub__(self, other):
        ResultNumerator = 0
        ResultDenominator = 0
        if (type(other) == type(int())):
            ResultNumerator = self.Numerator - other * self.Denominator
            ResultDenominator = self.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()
        else:
            ResultNumerator = self.Numerator * other.Denominator - other.Numerator * self.Denominator
            ResultDenominator = self.Denominator * other.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()

    # Multiply 2 fraction
    def __mul__(self, other):
        ResultNumerator = 0
        ResultDenominator = 0
        if (type(other) == type(int())):
            ResultNumerator = self.Numerator * other
            ResultDenominator = self.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()
        else:
            ResultNumerator = self.Numerator * other.Numerator
            ResultDenominator = self.Denominator * other.Denominator
            return Fraction(ResultNumerator, ResultDenominator).shortenFraction()

    def __truediv__(self, other):
        Result = Fraction(0, 1)
        Result.Numerator = self.Numerator * other.Denominator
        Result.Denominator = self.Denominator * other.Numerator
        return Result.shortenFraction()

    def __neg__(self):
        Result = Fraction(0, 1)
        Result.Numerator = self.Numerator * -1
        Result.Denominator = self.Denominator
        return Result

    # 9. Compare 2 fraction
    # Redefind equal operator
    def __eq__(self, other):
        return self.Numerator * other.Denominator == other.Numerator * self.Denominator

    # Redefind not equal operator
    def __ne__(self, other):
        return self.Numerator * other.Denominator != other.Numerator * self.Denominator

    # Redefind greater than operator
    def __gt__(self, other):
        return self.Numerator * other.Denominator > other.Numerator * self.Denominator

    # Redefind less than operator
    def __lt__(self, other):
        return self.Numerator * other.Denominator < other.Numerator * self.Denominator

    # Redefind greater than or equal operator
    def __ge__(self, other):
        return self.Numerator * other.Denominator >= other.Numerator * self.Denominator

    # Redefind less than or equal operator
    def __le__(self, other):
        return self.Numerator * other.Denominator <= other.Numerator * self.Denominator


if __name__ == '__main__':
    a = Fraction(2, 3)
    b = Fraction(1, 4)
    c = Fraction(3, 1)
    d = Fraction(2, 5)
    e = Fraction(2, 3)
    print(Fraction.findLargestFraction([a, b, c, d, e]))
    print(a + b)
