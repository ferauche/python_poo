from abc import ABCMeta, abstractmethod

class Transparencia(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def to_csv(self):
        pass

    @abstractmethod
    def to_txt(self):
        pass

