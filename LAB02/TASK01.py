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
        gcd = self.__findGCD(self.__numerator, self.__denominator)
        return Fraction(self.__numerator // gcd, self.__denominator // gcd)

    # print fraction
    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    # add 2 fractions & add fraction to number
    def __add__(self, other) -> Fraction:
        if type(int()) == type(other):
            new_numerator = self.__numerator + other * self.__denominator
            new_denominator = self.__denominator
        else:
            new_numerator = self.__numerator * other.denominator + other.numerator * self.__denominator
            new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator).__shortenFraction()

    # subtract 2 fractions & subtract fraction to number
    def __sub__(self, other) -> Fraction:
        if type(int()) == type(other):
            new_numerator = self.__numerator - other * self.__denominator
            new_denominator = self.__denominator
        else:
            new_numerator = self.__numerator * other.denominator - other.numerator * self.__denominator
            new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator).__shortenFraction()

    # multiply2 fractions & multiply fraction to number
    def __mul__(self, other) -> Fraction:
        if type(int()) == type(other):
            new_numerator = self.__numerator * other
            new_denominator = self.__denominator
        else:
            new_numerator = self.__numerator * other.numerator
            new_denominator = self.__denominator * other.denominator
        return Fraction(new_numerator, new_denominator).__shortenFraction()

    # divide fraction by fraction & divide fraction by number
    def __truediv__(self, other) -> Fraction:
        if type(int()) == type(other):
            new_numerator = self.__numerator
            new_denominator = self.__denominator * other
        else:
            new_numerator = self.__numerator * other.denominator
            new_denominator = self.__denominator * other.numerator
        return Fraction(new_numerator, new_denominator).__shortenFraction()

    # redefine the equal operator
    def __eq__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator == other
        else:
            return self.__numerator / self.__denominator == other.numerator / other.denominator

    # redefine the negative operator
    def __ne__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator != other
        else:
            return self.__numerator / self.__denominator != other.numerator / other.denominator

    # redefine the greater than operator
    def __gt__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator > other
        else:
            return self.__numerator / self.__denominator > other.numerator / other.denominator

    # redefine the greater than or equal operator
    def __ge__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator >= other
        else:
            return self.__numerator / self.__denominator >= other.numerator / other.denominator

    # redefine the less than operator
    def __lt__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator < other
        else:
            return self.__numerator / self.__denominator < other.numerator / other.denominator

    # redefine the less than or equal operator
    def __le__(self, other) -> bool:
        if type(int()) == type(other):
            return self.__numerator / self.__denominator <= other
        else:
            return self.__numerator / self.__denominator <= other.numerator / other.denominator

