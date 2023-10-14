from Register.PC import PC
from Register.Mem_Wb import Mem_Wb
from Register.If_Id import If_Id
from Register.Id_Ex import Id_Ex


class Circuit:
    def __init__(self):
        self.__PC = PC()
        self.__mem_wb = Mem_Wb()
        self.__if_id = If_Id()
        self.__id_ex = Id_Ex()

    def get_pc(self):
        return self.__PC

    def get_mem_wb(self):
        return self.__mem_wb

    def get_if_id(self):
        return self.__if_id

    def get_id_ex(self):
        return self.__id_ex
