class Staff:
    #Construtor
    def __init__(self, **kwargs):
        self.__ID = kwargs.get('id')
        self.__Name = kwargs.get('name')
        self.__BaseSalary = kwargs.get('base salary')
        self.__Products = kwargs.get('products')
        self.__MonthlySalary = kwargs.get('monthly salary')
