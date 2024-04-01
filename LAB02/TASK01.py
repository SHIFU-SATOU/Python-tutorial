class Fraction:
    # Initialization method
    def __init__(self, numerator: int, denominator: int):
        self.Numerator = numerator
        self.Denominator = denominator

    @property
    def Numerator(self) -> int:
        return self.Numerator

    @Numerator.setter
    def Numerator(self, new_value: int) -> None:
        self.Numerator = new_value

    @property
    def Denominator(self) -> int:
        return self.Denominator

    @Denominator.setter
    def Denominator(self, new_value: int) -> None:
        self.Denominator = new_value
