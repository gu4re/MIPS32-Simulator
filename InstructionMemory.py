from Memory import Memory


class InstructionMemory(Memory):

    __instruction_memory = {}

    @staticmethod
    def write(key, value):
        InstructionMemory.__instruction_memory[key] = value

    @staticmethod
    def read(key):
        return InstructionMemory.__instruction_memory.get(key, None)

    @staticmethod
    def print():
        print("|----------------INSTRUCTION MEMORY-----------------|")
        for key, value in InstructionMemory.__instruction_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")

    @staticmethod
    def generate_address():
        if len(InstructionMemory.__instruction_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(InstructionMemory.__instruction_memory.keys())[-1], 16) + 4)
