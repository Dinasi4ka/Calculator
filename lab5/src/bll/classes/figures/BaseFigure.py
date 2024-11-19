from abc import ABC, abstractmethod

class BaseFigure(ABC):
    def __init__(self, size: int):
        self.size = size

    @abstractmethod
    def get_two_d_art(self):
        pass

    @abstractmethod
    def get_three_d_art(self):
        pass