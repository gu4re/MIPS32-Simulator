from abc import ABC, abstractmethod


# Memory Interface
class Memory(ABC):

    @staticmethod
    @abstractmethod
    def write(key, value):
        pass

    @staticmethod
    @abstractmethod
    def read(key):
        pass

    @staticmethod
    @abstractmethod
    def print():
        pass

    @staticmethod
    @abstractmethod
    def generate_address():
        pass
