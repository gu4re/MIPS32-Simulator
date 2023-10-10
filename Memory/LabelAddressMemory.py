import time

from Memory import Memory
from datetime import datetime


class LabelAddressMemory(Memory):

    __label_address_memory = {}

    @staticmethod
    def write(key, value):
        LabelAddressMemory.__label_address_memory[key] = value
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[LabelAddressMemory]: Value '{value}' loaded at '{key}'.")

    @staticmethod
    def read(key):
        time.sleep(1)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[LabelAddressMemory]: Read address '{key}'.")
        return LabelAddressMemory.__label_address_memory.get(key, None)

    @staticmethod
    def print():
        print("|---------------LABEL ADDRESS MEMORY----------------|")
        for key, value in LabelAddressMemory.__label_address_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")
        time.sleep(2)

    @staticmethod
    def generate_address():
        if len(LabelAddressMemory.__label_address_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(LabelAddressMemory.__label_address_memory.keys())[-1], 16) + 4)
