class Staff:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Status = kwargs.get('Status', "Còn học")
