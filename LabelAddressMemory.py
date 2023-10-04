from Memory import Memory


class LabelAddressMemory(Memory):

    __label_address_memory = {}

    @staticmethod
    def write(key, value):
        LabelAddressMemory.__label_address_memory[key] = value

    @staticmethod
    def read(key):
        return LabelAddressMemory.__label_address_memory.get(key, None)

    @staticmethod
    def print():
        print("|---------------LABEL ADDRESS MEMORY----------------|")
        for key, value in LabelAddressMemory.__label_address_memory.items():
            print(f"| Key: {key}, Value: {value}")
        print("|---------------------------------------------------|")

    @staticmethod
    def generate_address():
        if len(LabelAddressMemory.__label_address_memory) == 0:
            return hex(0x0000)
        else:
            return hex(int(list(LabelAddressMemory.__label_address_memory.keys())[-1], 16) + 4)
