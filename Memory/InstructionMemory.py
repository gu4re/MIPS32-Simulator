import time

from Memory.Interface import Memory
from datetime import datetime


class InstructionMemory(Memory):
    def __init__(self):
        self.__instruction_memory = {}

    def write(self, key, value):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[InstructionMemory]: Value '{value}' loaded at '{key}'.")
        self.__instruction_memory[key] = value

    def read(self, key):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[InstructionMemory]: Read address '{key}'.")
        return self.__instruction_memory.get(key, None)

    def print(self):
        print("|----------------INSTRUCTION MEMORY-----------------|")
        for key, value in self.__instruction_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")
        time.sleep(0.2)

    def generate_address(self):
        if len(self.__instruction_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(self.__instruction_memory.keys())[-1], 16) + 4)
