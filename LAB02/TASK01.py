class Fraction:
    # Data components
    def __init__(self, **kwargs):
        self.__Numerator = int(kwargs.get('Tử số'))
        self.__Denominator = int(kwargs.get('Mẫu số'))