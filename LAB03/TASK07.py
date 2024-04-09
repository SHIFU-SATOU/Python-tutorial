class Clinic:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Doctors = []
        self.__Patients = []
        self.__Medicines = []


class Doctor:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__RentCost = kwargs.get('RentCost', 0.0)
        self.__Patients = []

    # Get ID of doctor
    @property
    def ID(self) -> str:
        return self.__ID

    # Get rent cost
    @property
    def RentCost(self) -> float:
        return self.__RentCost


class Patient:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Doctors = []
        self.__Medicines = []

    # Get ID of patient
    @property
    def ID(self) -> str:
        return self.__ID


class Medicine:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Price = kwargs.get('Price', 0.0)

    # Get ID of medicine
    @property
    def ID(self) -> str:
        return self.__ID