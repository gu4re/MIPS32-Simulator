from Memory import Memory


class DataMemory(Memory):

    __data_memory = {}

    @staticmethod
    def write(key, value):
        DataMemory.__data_memory[key] = value

    @staticmethod
    def read(key):
        return DataMemory.__data_memory.get(key, None)

    @staticmethod
    def print():
        print("|--------------------DATA MEMORY--------------------|")
        for key, value in DataMemory.__data_memory.items():
            print(f"| Key: {key}, Value: {value} ")
        print("|---------------------------------------------------|")

    @staticmethod
    def generate_address():
        if len(DataMemory.__data_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(DataMemory.__data_memory.keys())[-1], 16) + 4)
