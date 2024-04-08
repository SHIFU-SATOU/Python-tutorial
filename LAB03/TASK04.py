from abc import ABC, abstractmethod
class Point(ABC):
    # Constructor
    def __init__(self, **kwargs):
        self._X = kwargs.get('X', 0)
        self._Y = kwargs.get('Y', 0)

class Circle(Point):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._Radius = kwargs.get('Radius', 0)

