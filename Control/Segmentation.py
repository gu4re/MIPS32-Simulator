import time

from datetime import datetime
from library.colorama import Fore, Style
from Circuit import Circuit
from Control.ForwardingUnit import ForwardingUnit

import re


class Segmentation:

    def __init__(self, circuit: Circuit, forwarding_unit: ForwardingUnit):
        self.__circuit = circuit
        self.__forwarding_unit = forwarding_unit

    def fetch(self):
        content_pc = self.__circuit.get_pc().read()
        print(f"{datetime.now().strftime('[%H:%M:%S]')}[ControlUnit]:"
              f" Fetching PC ...")
        new_instruction = self.__circuit.get_instruction_memory().read(content_pc)
        if new_instruction is None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[Fetcher]: No more instructions left!")
            self.__circuit.get_if_id().clear()
            return False
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[Fetcher]: Instruction read is '{new_instruction}'")
        self.__circuit.get_if_id().write_instruction(new_instruction)
        self.__circuit.get_pc().update(content_pc)
        return True

    def decode(self, if_id, need_flush):
        if need_flush:
            self.__circuit.get_id_ex().clear()
            print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[Decoder]: Clear IDEX register.{Style.RESET_ALL}")
            return False, None
        if (if_id is not False
                and self.__circuit.get_if_id().read_instruction() is not None):
            if_id = self.__circuit.get_if_id().read_instruction()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction '{if_id}' ...")
            # Syscall path
            if if_id == "syscall":
                rt = self.__circuit.get_registers_memory().read("$a0")
                rs = self.__circuit.get_registers_memory().read("$v0")
                rs_rt = self.__forwarding_unit.check_ex_mem(["$a0", "$v0"], [rt, rs])
                rt = rs_rt.get("$a0", None)
                rs = rs_rt.get("$v0", None)
                rs_rt = self.__forwarding_unit.check_mem_wb(["$a0", "$v0"], [rt, rs])
                rt = rs_rt.get("$a0", None)
                rs = rs_rt.get("$v0", None)
                if rt is None or rs is None:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[ControlUnit]: Register '{'$a0' if rt is None else '$v0'}' "
                          f"provoked a bubble so Fetcher is returning None. {Style.RESET_ALL}")
                    return False, True
                self.__circuit.get_id_ex().write(if_id, new_rs=rs, new_rt=rt)
                return True, None
            cod_op = if_id.split()[0]
            if cod_op == "j":
                rd = re.split(r',\s*', if_id)[0].split()[1]
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', with "
                      f"destiny '{rd}', will be effective.")
                self.__circuit.get_id_ex().write(cod_op, rd, jump_on=True)
                return True, None
            if len(re.split(r',\s*', if_id)) == 3:
                rd, rs, rt = (re.split(r',\s*', if_id)[0].split()[1], re.split(r',\s*', if_id)[1],
                              re.split(r',\s*', if_id)[2])
                if cod_op == "bge":
                    rd_value, rs_value = (self.__circuit.get_registers_memory().read(rd),
                                          self.__circuit.get_registers_memory().read(rs))
                    rd_rs_values = self.__forwarding_unit.check_ex_mem([rd, rs],
                                                                       [rd_value, rs_value])
                    rd_value = rd_rs_values.get(rd, None)
                    rs_value = rd_rs_values.get(rs, None)
                    rd_rs_values = self.__forwarding_unit.check_mem_wb([rd, rs],
                                                                       [rd_value, rs_value])
                    rd_value = rd_rs_values.get(rd, None)
                    rs_value = rd_rs_values.get(rs, None)
                    if rd_value is None or rs_value is None:
                        raise Exception(f"Instruction '{cod_op}' should not provoked a bubble. {Style.RESET_ALL}")
                    jump_on = self.__circuit.get_conditional_alu().compare(rd_value, rs_value)
                    if jump_on:
                        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                              f"[Decoder]: Operation code '{cod_op}', with "
                              f"destiny '{rt}', will be effective.")
                    else:
                        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                              f"[Decoder]: Operation code '{cod_op}', with "
                              f"destiny '{rt}', will NOT be effective.")
                    self.__circuit.get_id_ex().write(cod_op, rt, jump_on=jump_on)
                    return True, None
                if cod_op == "addi":
                    rs_value = self.__circuit.get_registers_memory().read(rs)
                    new_rs_value = (self.__forwarding_unit.check_ex_mem([rs],
                                                                        [rs_value])
                                    .get(rs, None))
                    if new_rs_value is None:
                        new_rs_value = (self.__forwarding_unit.check_mem_wb([rs],
                                                                            [new_rs_value])
                                        .get(rs, None))
                        if new_rs_value is None:
                            raise Exception(f"Instruction '{cod_op}' should not provoked a bubble. {Style.RESET_ALL}")
                    print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[Decoder]: Operation code '{cod_op}', register of "
                          f"destiny '{rd}', first operand '{new_rs_value}', second operand "
                          f"'{rt}'")
                    self.__circuit.get_id_ex().write(cod_op, rd, new_rs_value, rt)
                    return True, None
                else:
                    rs_value, rt_value = (self.__circuit.get_registers_memory().read(rs),
                                          self.__circuit.get_registers_memory().read(rt))
                    rs_rt_values = self.__forwarding_unit.check_ex_mem([rs, rt],
                                                                       [rs_value, rt_value])
                    rs_value = rs_rt_values.get(rs, None)
                    rt_value = rs_rt_values.get(rt, None)
                    rs_rt_values = self.__forwarding_unit.check_mem_wb([rs, rt],
                                                                       [rs_value, rt_value])
                    rs_value = rs_rt_values.get(rs, None)
                    rt_value = rs_rt_values.get(rt, None)
                    if rs_value is None or rt_value is None:
                        raise Exception(f"Instruction '{cod_op}' should not provoked a bubble. {Style.RESET_ALL}")
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs_value}', second operand "
                      f"'{rt_value}'")
                self.__circuit.get_id_ex().write(cod_op, rd, rs_value, rt_value)
                return True, None
                # instruction, destiny, op1, op2
            elif len(re.split(r',\s*', if_id)) == 2:
                if cod_op == "sw":
                    rs, rd = re.split(r',\s*', if_id)[0].split()[1], re.split(r',\s*', if_id)[1]
                    rs_value = self.__circuit.get_registers_memory().read(rs)
                    rs_value = (self.__forwarding_unit.check_ex_mem([rs],
                                                                    [rs_value])
                                .get(rs, None))
                    if rs_value is None:
                        rs_value = (self.__forwarding_unit.check_mem_wb([rs],
                                                                        [rs_value])
                                    .get(rs, None))
                    if rs_value is None:
                        print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                              f"[ControlUnit]: Register '{rs}' provoked a bubble. {Style.RESET_ALL}")
                        return False, True
                    mem_address, which_mem = self.__circuit.get_label_address_memory().read(rd)
                    if which_mem != 'D':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                    self.__circuit.get_id_ex().write(cod_op, mem_address, rs_value)
                    return True, None
                elif cod_op == "la" or cod_op == "lw":
                    rd, rs = re.split(r',\s*', if_id)[0].split()[1], re.split(r',\s*', if_id)[1]
                    mem_address, which_mem = self.__circuit.get_label_address_memory().read(rs)
                    rs = mem_address
                    if which_mem != 'D':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                else:
                    rd, rs = re.split(r',\s*', if_id)[0].split()[1], re.split(r',\s*', if_id)[1]
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}'")
                self.__circuit.get_id_ex().write(cod_op, rd, rs)
                return True, None
        self.__circuit.get_id_ex().clear()
        return False, None

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
            elif ex_mem.read_cod_op() == "la" or ex_mem.read_cod_op() == "lw":
                mem_wb.write(ex_mem.read_destination(), self.__circuit.get_data_memory()
                             .read(ex_mem.read_address_or_value()))
                return True
            elif ex_mem.read_cod_op() == "sw":
                self.__circuit.get_data_memory().write(ex_mem.read_destination(), ex_mem.read_address_or_value())
                return False
        self.__circuit.get_mem_wb().clear()
        return False

    def execute(self, id_ex):
        if id_ex is not False:
            id_ex = self.__circuit.get_id_ex()
            cod_op = id_ex.read_cod_op()
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Executing '{cod_op}' instruction ...")
            rd, rs, rt = id_ex.read_rd(), id_ex.read_rs(), id_ex.read_rt()
            if cod_op == "syscall":
                v0_value = id_ex.read_rs()
                # I/O operations
                if int(v0_value) == 4 or int(v0_value) == 1:
                    a0_value = id_ex.read_rt()
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Output]: {a0_value}{Style.RESET_ALL}")
                    return False, None
                elif int(v0_value) == 5:
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Input]: {Style.RESET_ALL}", end="")
                    inp = int(input(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    # Avoid infinite loop
                    if inp == 0 or inp == 1:
                        raise Exception("Expected number above 1. Aborting program to avoid infinite loop ...")
                    self.__circuit.get_aux_ex_mem().write(cod_op, "$v0", inp, True)
                    return True, None
                else:
                    raise Exception("SysCall wrong code ...")
            elif cod_op == "bge" or cod_op == "j":
                if id_ex.read_jump_on() is True:
                    time.sleep(0.1)
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[ControlUnit]: Address calculated to jump.{Style.RESET_ALL}")
                    address_to_go, which_mem = self.__circuit.get_label_address_memory().read(id_ex.read_rd())
                    if which_mem != 'I':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                    # Need a correction changing PC registry so (address_to_go - 4 + 4)
                    self.__circuit.get_pc().update(hex(int(address_to_go, 16) - 4))
                    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[ControlUnit]: New address stored in PC.{Style.RESET_ALL}")
                    return False, True
                return False, None
            elif cod_op == "addi" or cod_op == "add":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().add(int(rs), int(rt)), True)
                return True, None
            elif cod_op == "mul":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().multiply(int(rs), int(rt)), True)
                return True, None
            elif cod_op == "sub":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().subtract(int(rs), int(rt)), True)
                return True, None
            elif cod_op == "li" or cod_op == "la" or cod_op == "sw" or cod_op == "lw":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd, rs, True)
                return True, None
        self.__circuit.get_aux_ex_mem().clear(True)
        return False, None

    def write_back(self, mem_wb):
        if mem_wb is not False:
            mem_wb = self.__circuit.get_mem_wb()
            self.__circuit.get_registers_memory().write(mem_wb.read_destination(),
                                                        mem_wb.read_address_or_value())
