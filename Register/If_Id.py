import time


class If_Id:
    def __init__(self):
        self.__instruction = None

    def read_instruction(self):
        time.sleep(1)
        return self.__instruction

    def write_instruction(self, new_instruction):
        time.sleep(1)
        self.__instruction = new_instruction
