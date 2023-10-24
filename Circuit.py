from Register.PC import PC
from Register.MemWb import MemWb
from Register.IfId import IfId
from Register.IdEx import IdEx
from Register.ExMem import ExMem
from ALU.BasicALU import BasicALU
from ALU.ConditionalALU import ConditionalALU
from Memory.DataMemory import DataMemory
from Memory.InstructionMemory import InstructionMemory
from Memory.LabelAddressMemory import LabelAddressMemory
from Memory.RegistersMemory import RegistersMemory


class Circuit:
    def __init__(self):
        self.__PC = PC()
        self.__mem_wb = MemWb()
        self.__if_id = IfId()
        self.__id_ex = IdEx()
        self.__ex_mem = ExMem()
        self.__aux_ex_mem = ExMem()
        self.__basic_alu = BasicALU()
        self.__conditional_alu = ConditionalALU()
        self.__data_memory = DataMemory()
        self.__instruction_memory = InstructionMemory()
        self.__label_address_memory = LabelAddressMemory()
        self.__registers_memory = RegistersMemory()

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

    def get_data_memory(self):
        return self.__data_memory

    def get_instruction_memory(self):
        return self.__instruction_memory

    def get_label_address_memory(self):
        return self.__label_address_memory

    def get_registers_memory(self):
        return self.__registers_memory
