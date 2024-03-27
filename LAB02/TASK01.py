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

    #Redefine the output method
    def __str__(self):
        return f"{self.__Numerator}/{self.__Denominator}"
