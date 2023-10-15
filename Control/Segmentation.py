from Memory.RegistersMemory import RegistersMemory
from datetime import datetime
from Memory.DataMemory import DataMemory
from Memory.InstructionMemory import InstructionMemory
from Memory.LabelAddressMemory import LabelAddressMemory
from library.colorama import Fore, Style
from Circuit import Circuit
from Control.ShortCircuitUnit import ShortCircuitUnit


class Segmentation:

    def __init__(self, circuit: Circuit, short_circuit_unit: ShortCircuitUnit):
        self.__circuit = circuit
        self.__short_circuit_unit = short_circuit_unit

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
            if_id = self.__circuit.get_if_id().read_instruction()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction '{if_id}' ...")
            # Syscall path
            if if_id == "syscall":
                rt = self.__short_circuit_unit.check_ex_mem(["$v0", "$a0"]).get("$a0")
                rs = self.__short_circuit_unit.check_mem_wb(["$v0", "$a0"]).get("$v0")
                self.__circuit.get_id_ex().write(if_id, new_rs=rs, new_rt=rt)
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
            ex_mem = self.__circuit.get_ex_mem()
            mem_wb = self.__circuit.get_mem_wb()
            if ex_mem.read_cod_op() not in instruction_collection:
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[DataMemory]: Ignoring '{ex_mem.read_cod_op()}' instruction ...")
                mem_wb.write(ex_mem.read_destination(), ex_mem.read_address_or_value())
                return True
            elif ex_mem.read_cod_op() == "la":
                mem_wb.write(ex_mem.read_destination(), DataMemory.read(ex_mem.read_address_or_value()))
                return False
            elif ex_mem.read_cod_op() == "sw":
                DataMemory.write(ex_mem.read_destination(), ex_mem.read_address_or_value())
                return False
            # TODO: Needs implementation of lw
        return False

    def execute(self, id_ex):
        if id_ex is not False:
            id_ex = self.__circuit.get_id_ex()
            cod_op = id_ex.read_cod_op()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Executing '{cod_op}' instruction ...")
            if cod_op == "syscall":
                v0_value = id_ex.read_rs()
                # I/O operations
                if int(v0_value) == 4:
                    a0_value = id_ex.read_rt()
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Output]: {a0_value}{Style.RESET_ALL}")
                    return False
                elif int(v0_value) == 5:
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Input]: {Style.RESET_ALL}", end="")
                    inp = int(input(f"{Fore.YELLOW}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    self.__circuit.get_ex_mem().write(cod_op, "$v0", inp)
                    return True
                else:
                    raise Exception("SysCall wrong code ...")
                    # TODO missing SysCall code 1 implementation
            rd, rs, rt = id_ex.read_rd(), id_ex.read_rs(), id_ex.read_rt()
            if cod_op == "addi":
                self.__circuit.get_ex_mem().write(cod_op, rd,
                                                  self.__circuit.get_basic_alu().add(int(rs), int(rt)))
                return True
            elif cod_op == "mul":
                self.__circuit.get_ex_mem().write(cod_op, rd,
                                                  self.__circuit.get_basic_alu().multiply(int(rs), int(rt)))
                return True
            elif cod_op == "sub":
                self.__circuit.get_ex_mem().write(cod_op, rd,
                                                  self.__circuit.get_basic_alu().subtract(int(rs), int(rt)))
                return True
            elif cod_op == "li" or cod_op == "la" or cod_op == "sw":
                self.__circuit.get_ex_mem().write(cod_op, rd, rs)
                return True
        return False

    def write_back(self, mem_wb):
        if mem_wb is not False:
            mem_wb = self.__circuit.get_mem_wb()
            RegistersMemory.write(mem_wb.read_destination(),
                                  mem_wb.read_address_or_value())
