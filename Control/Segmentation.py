from Register.Ex_Mem import Ex_Mem
from ALU.BasicALU import BasicALU
from Memory.RegistersMemory import RegistersMemory
from datetime import datetime
from Memory.DataMemory import DataMemory
from Memory.InstructionMemory import InstructionMemory
from Memory.LabelAddressMemory import LabelAddressMemory
from library.colorama import Fore, Style
from Circuit import Circuit


class Segmentation:

    def __init__(self, circuit: Circuit):
        self.__circuit = circuit

    def fetch(self):
        content_pc = self.__circuit.get_pc().read()
        print(f"{datetime.now().strftime('[%H:%M:%S]')}[ControlUnit]:"
              f" Fetching PC ...")
        new_instruction = InstructionMemory.read(content_pc)
        if new_instruction is None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[Fetcher]: No more instructions left!")
            return False
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[Fetcher]: Instruction read is '{new_instruction}'")
        self.__circuit.get_if_id().write_instruction(new_instruction)
        self.__circuit.get_pc().update(content_pc)
        return True

    def decode(self, if_id):
        if if_id is not False:
            if_id = if_id.read_instruction()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction '{if_id}' ...")
            # Syscall path
            if if_id == "syscall":
                self.__circuit.get_id_ex().write(if_id, rs=RegistersMemory.read("$v0"),
                                                 rt=RegistersMemory.read("$a0"))
                return True
                # TODO Need to resolve RAW provoked by syscall
            cod_op = if_id.split()[0]
            if len(if_id.split()[1].split(',')) == 3:
                rd, rs, rt = if_id.split()[1].split(',')
                if cod_op == "addi":
                    rs = RegistersMemory.read(rs)
                else:
                    rs, rt = RegistersMemory.read(rs), RegistersMemory.read(rt)
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}', second operand "
                      f"'{rt}'")
                self.__circuit.get_id_ex().write(cod_op, rd, rs, rt)
                return True
                # instruction, destiny, op1, op2
            elif len(if_id.split()[1].split(',')) == 2:
                if cod_op == "sw":
                    rs, rd = if_id.split()[1].split(',')
                    rs = RegistersMemory.read(rs)
                    mem_address, which_mem = LabelAddressMemory.read(rd)
                    rd = mem_address
                    if which_mem != 'D':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                elif cod_op == "la":
                    rd, rs = if_id.split()[1].split(',')
                    mem_address, which_mem = LabelAddressMemory.read(rs)
                    rs = mem_address
                    if which_mem != 'D':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                else:
                    rd, rs = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}'")
                self.__circuit.get_id_ex().write(cod_op, rd, rs)
                return True
            # TODO: Needs comparison of jump here
            # TODO: Calculate address to jump and put a print simulating in EX
        return False

    def memory(self, ex_mem):
        if ex_mem is not False:
            instruction_collection = ["lw", "la", "sw"]
            mem_wb = self.__circuit.get_mem_wb()
            if ex_mem.read_cod_op() not in instruction_collection:
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[DataMemory]: Ignoring '{ex_mem.read_cod_op()}' instruction ...")
                mem_wb.write_destination(ex_mem.read_destination())
                mem_wb.write_value(ex_mem.read_address_or_value())
                return True
            elif ex_mem.read_cod_op() == "la":
                mem_wb.write_destination(ex_mem.read_destination())
                mem_wb.write_value(DataMemory.read(ex_mem.read_address_or_value()))
                return False
            elif ex_mem.read_cod_op() == "sw":
                DataMemory.write(ex_mem.read_destination(), ex_mem.read_address_or_value())
                return False
            # TODO: Needs implementation of lw
        return False

    @staticmethod
    def execute(id_ex):
        if id_ex is not None:
            cod_op = id_ex.read_cod_op()
            if cod_op == "syscall":
                v0_value = id_ex.read_rs()
                # I/O operations
                if int(v0_value) == 4:
                    a0_value = id_ex.read_rt()
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Output]: {a0_value}{Style.RESET_ALL}")
                    return None
                elif int(v0_value) == 5:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Input]: {Style.RESET_ALL}", end="")
                    inp = int(input(f"{Fore.YELLOW}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    return Ex_Mem(cod_op, "$v0", inp)
                else:
                    raise Exception("SysCall wrong code ...")
                    # TODO missing SysCall code 1 implementation
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Executing '{cod_op}' instruction ...")
            rd, rs, rt = id_ex.read_rd(), id_ex.read_rs(), id_ex.read_rt()
            if cod_op == "addi":
                return Ex_Mem(cod_op, rd, BasicALU.add(int(rs), int(rt)))
            elif cod_op == "mul":
                return Ex_Mem(cod_op, rd, BasicALU.multiply(int(rs), int(rt)))
            elif cod_op == "sub":
                return Ex_Mem(cod_op, rd, BasicALU.subtract(int(rs), int(rt)))
            elif cod_op == "li" or cod_op == "la" or cod_op == "sw":
                return Ex_Mem(cod_op, id_ex.read_rd(), id_ex.read_rs())
        return None

    def write_back(self, mem_wb):
        if mem_wb is not False:
            RegistersMemory.write(self.__circuit.get_mem_wb().read_destination(),
                                  self.__circuit.get_mem_wb().read_value())
