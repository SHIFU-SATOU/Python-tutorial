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
        self.__Patients = []

    # Get ID of doctor
    def __str__(self) -> str:
        return f"ID: {self.__ID} | Họ và tên: {self.__Name}"


class Patient:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Doctors = []
        self.__Medicines = []


class Medicine:
    # Constructor
    def __init__(self, **kwargs):
        self.__ID = str(kwargs.get('ID'))
        self.__Name = kwargs.get('Name', 'Trống')
        self.__Price = kwargs.get('Price', 0.0)
