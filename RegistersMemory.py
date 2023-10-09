import time

from Memory import Memory
from datetime import datetime


class RegistersMemory(Memory):

    __registers_memory = {
        "$t": [0] * 10,
        "$a": [0] * 4,
        "$v": [0, 0]
    }

    @staticmethod
    def write(register, value):
        time.sleep(1)
        register_type, register_num = register[:-1], int(register[-1])
        RegistersMemory.__registers_memory[register_type][register_num] = value
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[RegistersMemory]: Value '{value}' loaded at '{register}'.")

    @staticmethod
    def read(register):
        time.sleep(1)
        register_type, register_num = register[:-1], int(register[-1])
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[RegistersMemory]: Read register '{register}'.")
        return RegistersMemory.__registers_memory[register_type][register_num]

    @staticmethod
    def print():
        for key, value in RegistersMemory.__registers_memory.items():
            for v in value:
                print(f"Key: {key}, Value: {v}")

    # Not necessary in this case
    @staticmethod
    def generate_address():
        pass
