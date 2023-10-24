import time

from Memory.Memory import Memory
from datetime import datetime


class RegistersMemory(Memory):
    def __init__(self):
        self.__registers_memory = {
            "$t": [None] * 10,
            "$a": [None] * 4,
            "$v": [None, None]
        }

    def write(self, register, value):
        time.sleep(0.1)
        register_type, register_num = register[:-1], int(register[-1])
        self.__registers_memory[register_type][register_num] = value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[RegistersMemory]: Value '{value}' loaded at '{register}'.")

    def read(self, register):
        time.sleep(0.1)
        register_type, register_num = register[:-1], int(register[-1])
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[RegistersMemory]: Read register '{register}'.")
        return self.__registers_memory[register_type][register_num]

    def print(self):
        for key, value in self.__registers_memory.items():
            for v in value:
                print(f"Key: {key}, Value: {v}")

    # Not necessary in this case
    def generate_address(self):
        pass
