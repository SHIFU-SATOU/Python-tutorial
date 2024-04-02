class Triangle:
    pass


class Triangle:

    # Constructor
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    # print triangle
    def __str__(self):
        return f"{self.__a}, {self.__b}, {self.__c}"
