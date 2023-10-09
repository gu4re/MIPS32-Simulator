import time

from Memory import Memory
from datetime import datetime


class DataMemory(Memory):

    __data_memory = {}

    @staticmethod
    def write(key, value):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[DataMemory]: Value '{value}' loaded at '{key}'.")
        DataMemory.__data_memory[key] = value

    @staticmethod
    def read(key):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[DataMemory]: Read address '{key}'.")
        return DataMemory.__data_memory.get(key, None)

    @staticmethod
    def print():
        print("|--------------------DATA MEMORY--------------------|")
        for key, value in DataMemory.__data_memory.items():
            print(f"| Key: {key}, Value: {value} ")
        print("|---------------------------------------------------|")
        time.sleep(2)

    @staticmethod
    def generate_address():
        if len(DataMemory.__data_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(DataMemory.__data_memory.keys())[-1], 16) + 4)
