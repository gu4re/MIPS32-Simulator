import time

from Memory.Interface import Memory
from datetime import datetime


class InstructionMemory(Memory):

    __instruction_memory = {}

    @staticmethod
    def write(key, value):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[InstructionMemory]: Value '{value}' loaded at '{key}'.")
        InstructionMemory.__instruction_memory[key] = value

    @staticmethod
    def read(key):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[InstructionMemory]: Read address '{key}'.")
        return InstructionMemory.__instruction_memory.get(key, None)

    @staticmethod
    def print():
        print("|----------------INSTRUCTION MEMORY-----------------|")
        for key, value in InstructionMemory.__instruction_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")
        time.sleep(2)

    @staticmethod
    def generate_address():
        if len(InstructionMemory.__instruction_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(InstructionMemory.__instruction_memory.keys())[-1], 16) + 4)
