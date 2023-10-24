from abc import ABC, abstractmethod


# Memory Interface
class Memory(ABC):

    @abstractmethod
    def write(self, key, value):
        pass

    @abstractmethod
    def read(self, key):
        pass

    @abstractmethod
    def print(self):
        pass

    @abstractmethod
    def generate_address(self):
        pass
