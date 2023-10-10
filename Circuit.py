from Register.PC import PC
from Register.Mem_Wb import Mem_Wb


class Circuit:
    def __init__(self):
        self.__PC = PC()
        self.__mem_wb = Mem_Wb()

    def get_pc(self):
        return self.__PC

    def get_mem_wb(self):
        return self.__mem_wb
