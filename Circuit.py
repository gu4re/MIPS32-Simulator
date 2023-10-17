from Register.PC import PC
from Register.Mem_Wb import Mem_Wb
from Register.If_Id import If_Id
from Register.Id_Ex import Id_Ex
from Register.Ex_Mem import Ex_Mem
from ALU.BasicALU import BasicALU
from ALU.ConditionalALU import ConditionalALU


class Circuit:
    def __init__(self):
        self.__PC = PC()
        self.__mem_wb = Mem_Wb()
        self.__if_id = If_Id()
        self.__id_ex = Id_Ex()
        self.__ex_mem = Ex_Mem()
        self.__aux_ex_mem = Ex_Mem()
        self.__basic_alu = BasicALU()
        self.__conditional_alu = ConditionalALU()

    def get_pc(self):
        return self.__PC

    def get_mem_wb(self):
        return self.__mem_wb

    def get_if_id(self):
        return self.__if_id

    def get_id_ex(self):
        return self.__id_ex

    def get_ex_mem(self):
        return self.__ex_mem

    def get_basic_alu(self):
        return self.__basic_alu

    def get_aux_ex_mem(self):
        return self.__aux_ex_mem

    def get_conditional_alu(self):
        return self.__conditional_alu
