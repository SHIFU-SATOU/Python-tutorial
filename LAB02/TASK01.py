from fractions import Fraction


class Fraction:
    # Initialization method
    def __init__(self, numerator: int, denominator: int):
        self.__numerator = numerator
        self.__denominator = denominator

    # get numerator
    @property
    def numerator(self) -> int:
        return self.__numerator

    # set numerator
    @numerator.setter
    def numerator(self, new_value: int) -> None:
        self.__numerator = new_value

    # get denominator
    @property
    def denominator(self) -> int:
        return self.__denominator

    # set denominator
    @denominator.setter
    def denominator(self, new_value: int) -> None:
        self.__denominator = new_value

    # find greatest common divisor
    @staticmethod
    def __findGCD(a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def __shortenFraction(self) -> Fraction:
        GCD = self.__findGCD(self.__numerator, self.__denominator)
        return Fraction(self.__numerator // GCD, self.__denominator // GCD)

    # print fraction
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    # add 2 fractions & add fraction to number
    def __add__(self, other) -> Fraction:
        new_numerator = 0
        new_denominator = 0
        if type(int()) == type(other):
            new_numerator = self.__numerator + other * self.__denominator
        else:
            new_numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
            new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)

    # subtract 2 fractions & subtract fraction to number
    def __sub__(self, other) -> Fraction:
        new_numerator = 0
        new_denominator = 0
        if type(int()) == type(other):
            new_numerator = self.__numerator - other * self.__denominator
        else:
            new_numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
            new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator)
