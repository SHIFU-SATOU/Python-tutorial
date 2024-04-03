class Circle:
    # constructor
    def __init__(self, r: int) -> None:
        self.__r = r

    # print info of circle
    def __str__(self)->str:
        return f"r = {self.__r}"

