from Register.If_Id import If_Id
from Register.Id_Ex import Id_Ex
from Register.Ex_Mem import Ex_Mem
from Register.Mem_Wb import Mem_Wb
from ALU.BasicALU import BasicALU
from Memory.RegistersMemory import RegistersMemory
from datetime import datetime
from Memory.DataMemory import DataMemory
from Memory.InstructionMemory import InstructionMemory
from Memory.LabelAddressMemory import LabelAddressMemory
from Register.PC import PC
from library.colorama import Fore, Style


class Segmentation:

    @staticmethod
    def fetch(pc):
        print(f"{datetime.now().strftime('[%H:%M:%S]')}[ControlUnit]:"
              f" Fetching PC...")
        instruction = InstructionMemory.read(pc)
        if instruction is None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: No more instructions left!")
            return None
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Instruction read is '{instruction}'")
        PC.update(pc)
        return If_Id(instruction)

    @staticmethod
    def decode(if_id):
        if if_id is not None:
            if_id = if_id.read()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction '{if_id}' ...")
            # Syscall path
            if if_id == "syscall":
                return Id_Ex(if_id, rs=RegistersMemory.read("$v0"), rt=RegistersMemory.read("$a0"))
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
                return Id_Ex(cod_op, rd, rs, rt)
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
                return Id_Ex(cod_op, rd, rs)
            # TODO: Needs comparison of jump here
        return None

    @staticmethod
    def memory(ex_mem):
        if ex_mem is not None:
            instruction_collection = ["lw", "la", "sw"]
            if ex_mem.read_cod_op() not in instruction_collection:
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[DataMemory]: Ignoring '{ex_mem.read_cod_op()}' instruction ...")
                return Mem_Wb(ex_mem.read_destination(), ex_mem.read_address_or_value())
            elif ex_mem.read_cod_op() == "la":
                return Mem_Wb(ex_mem.read_destination(),
                              DataMemory.read(ex_mem.read_address_or_value()))
            elif ex_mem.read_cod_op() == "sw":
                DataMemory.write(ex_mem.read_destination(), ex_mem.read_address_or_value())
                return None
            # TODO: Needs implementation of lw
        return None

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

    @staticmethod
    def write_back(mem_wb):
        if mem_wb is not None:
            RegistersMemory.write(mem_wb.read_destination(), mem_wb.read_value())
