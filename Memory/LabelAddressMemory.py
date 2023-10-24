import time

from Memory.Memory import Memory
from datetime import datetime


class LabelAddressMemory(Memory):
    def __init__(self):
        self.__label_address_memory = {}

    def write(self, key, value):
        self.__label_address_memory[key] = value
        time.sleep(0.1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[LabelAddressMemory]: Value '{value}' loaded at '{key}'.")

    def read(self, key):
        time.sleep(0.1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[LabelAddressMemory]: Read address '{key}'.")
        return self.__label_address_memory.get(key, None)

    def print(self):
        print("|---------------LABEL ADDRESS MEMORY----------------|")
        for key, value in self.__label_address_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")
        time.sleep(0.2)

    def generate_address(self):
        if len(self.__label_address_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(self.__label_address_memory.keys())[-1], 16) + 4)
