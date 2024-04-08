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

    # Get integer part of mixed number
    @property
    def Number(self) -> int:
        return self.__Number

    # Print mixed number
    def __str__(self) -> str:
        return f"{self.__Number} {self._Numerator}/{self._Denominator}"

    # Define the addition operator of mixed number
    def __add__(self, other) -> MixedNumber:
        if type(other) == type(int()):
            return MixedNumber(self._Numerator, self._Denominator, self.__Number + other)
        elif other.__class__.__name__ == 'MixedNumber':
            NewFraction = Fraction(self._Numerator * other.Denominator + other.Numerator * self._Denominator,
                                   self._Denominator * other.Denominator).shortenFraction()
            return MixedNumber(NewFraction.Numerator, NewFraction.Denominator, self.__Number + other.Number)
        elif other.__class__.__name__ == 'Fraction':
            NewFraction = Fraction(self._Numerator * other.Denominator + other.Numerator * self._Denominator,
                                   self._Denominator * other.Denominator).shortenFraction()
            return MixedNumber(NewFraction.Numerator, NewFraction.Denominator, self.__Number)

    # Define the subtract operator of mixed number
    def __sub__(self, other) -> MixedNumber:
        if type(other) == type(int()):
            return MixedNumber(self._Numerator, self._Denominator, self.__Number - other)
        elif other.__class__.__name__ == 'MixedNumber':
            NewFraction = Fraction(self._Numerator * other.Denominator - other.Numerator * self._Denominator,
                                   self._Denominator * other.Denominator).shortenFraction()
            return MixedNumber(NewFraction.Numerator, NewFraction.Denominator, self.__Number - other.Number)
        elif other.__class__.__name__ == 'Fraction':
            NewFraction = Fraction(self._Numerator * other.Denominator - other.Numerator * self._Denominator,
                                   self._Denominator * other.Denominator).shortenFraction()
            return MixedNumber(NewFraction.Numerator, NewFraction.Denominator, self.__Number)

    # Define mutiply operator of mixed number
    def __mul__(self, other) -> MixedNumber:
        if type(other) == type(int()):
            return MixedNumber(self._Numerator, self._Denominator, self.__Number * other)
        elif other.__class__.__name__ == 'MixedNumber':
            return MixedNumber(self._Numerator * other.Numerator, self._Denominator * other.Denominator,
                               self.__Number * other.Number)
        elif other.__class__.__name__ == 'Fraction':
            return MixedNumber(self._Numerator * other.Numerator, self._Denominator * other.Denominator, self.__Number)

    # Define divide operator of mixed number
    def __truediv__(self, other) -> MixedNumber:
        if type(other) == type(int()):
            return MixedNumber(self._Numerator, self._Denominator, self.__Number / other)
        elif other.__class__.__name__ == 'MixedNumber':
            return MixedNumber(self._Numerator * other.Denominator, self._Denominator * other.Numerator,
                               self.__Number / other.Number)
        elif other.__class__.__name__ == 'Fraction':
            return MixedNumber(self._Numerator * other.Denominator, self._Denominator * other.Numerator, self.__Number)

    # Definde equal operator of mixed number
    def __eq__(self, other) -> bool:
        if type(other) == type(int()):
            return self.__Number + self._Numerator / self._Denominator == other
        elif other.__class__.__name__ == 'MixedNumber':
            return self.__Number == other.Number and self._Numerator == other.Numerator and self._Denominator == other.Denominator
        elif other.__class__.__name__ == 'Fraction':
            return self.__Number + self._Numerator / self._Denominator == other.Numerator / other.Denominator

    # Definde not equal operator of mixed number
    def __ne__(self, other) -> bool:
        if type(other) == type(int()):
            return self.__Number + self._Numerator / self._Denominator != other
        elif other.__class__.__name__ == 'MixedNumber':
            return self.__Number != other.Number and self._Numerator != other.Numerator and self._Denominator != other.Denominator
        elif other.__class__.__name__ == 'Fraction':
            return self.__Number + self._Numerator / self._Denominator != other.Numerator / other.Denominator

    # Definde greater than operator of mixed number
    def __gt__(self, other) -> bool:
        if type(other) == type(int()):
            return self.__Number + self._Numerator / self._Denominator > other
        elif other.__class__.__name__ == 'MixedNumber':
            return self.__Number > other.Number and self._Numerator > other.Numerator and self._Denominator > other.Denominator
        elif other.__class__.__name__ == 'Fraction':
            return self.__Number + self._Numerator / self._Denominator > other.Numerator / other.Denominator

    # Definde greater than or equal operator of mixed number
    def __ge__(self, other) -> bool:
        if type(other) == type(int()):
            return self.__Number + self._Numerator / self._Denominator >= other
        elif other.__class__.__name__ == 'MixedNumber':
            return self.__Number >= other.Number and self._Numerator >= other.Numerator and self._Denominator >= other.Denominator
        elif other.__class__.__name__ == 'Fraction':
            return self.__Number + self._Numerator / self._Denominator >= other.Numerator / other.Denominator

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
    b2 = MixedNumber(4, 4, 4)
    # Convert fraction a to mixed number
    print(f"-Phân số a sau khi chuyển sang hỗn số: {MixedNumber.convertFractionToMixedNumber(a)}")
    # Convert mixed number b to fraction
    print(f"-Hỗn số b sau khi chuyển sang phân số: {b.convertMixedNumberToFraction()}")
    # Test addition operator of mixed number
    print(f"-Hỗn số b cộng phân số a: {b + a}")
    print(f"-Hỗn số b cộng hỗn số b2: {b + b2}")
    print(f"-Hỗn số b cộng 5: {b + 5}")
    # Test substract operator of mixed number
    print(f"-Hỗn số b trừ phân số a: {b - a}")
    print(f"-Hỗn số b2 trừ hỗn số b: {b2 - b}")
    print(f"-Hỗn số b trừ 5: {b - 5}")
    # Test multiply operator of mixed number
    print(f"-Hỗn số b nhân phân số a: {b * a}")
    print(f"-Hỗn số b2 nhân hỗn số b: {b2 * b}")
    print(f"-Hỗn số b nhân 5: {b * 5}")
    # Test divide operator of mixed number
    print(f"-Hỗn số b chia phân số a: {b / a}")
    print(f"-Hỗn số b2 chia hỗn số b: {b2 / b}")
    print(f"-Hỗn số b chia 5: {b / 5}")
    # Test equal operator of mixed number
    print(f"-Hỗn số b có bằng phân số a? {b == a}")
    print(f"-Hỗn số b có bằng hỗn số b 2? {b == b2}")
    print(f"-Hỗn số b có bằng 5? {b == 5}")
    # Test not equal operator of mixed number
    print(f"-Hỗn số b có khác phân số a? {b != a}")
    print(f"-Hỗn số b có khác hỗn số b 2? {b != b2}")
    print(f"-Hỗn số b có khác 5? {b != 5}")
    # Test greater than operator of mixed number
    print(f"-Hỗn số b có lớn hơn phân số a? {b > a}")
    print(f"-Hỗn số b có lớn hơn hỗn số b 2? {b > b2}")
    print(f"-Hỗn số b có lớn hơn 5? {b > 5}")
