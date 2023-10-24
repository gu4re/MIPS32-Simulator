import time

from Memory.Memory import Memory
from datetime import datetime


class DataMemory(Memory):
    def __init__(self):
        self.__data_memory = {}

    def write(self, key, value):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[DataMemory]: Value '{value}' loaded at '{key}'.")
        self.__data_memory[key] = value

    def read(self, key):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[DataMemory]: Read address '{key}'.")
        return self.__data_memory.get(key, None)

    def print(self):
        print("|--------------------DATA MEMORY--------------------|")
        for key, value in self.__data_memory.items():
            print(f"| Key: {key}, Value: {value} ")
        print("|---------------------------------------------------|")
        time.sleep(0.2)

    def generate_address(self):
        if len(self.__data_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(self.__data_memory.keys())[-1], 16) + 4)
