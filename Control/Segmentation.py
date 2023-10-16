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
                rt = RegistersMemory.read("$a0")
                rs = RegistersMemory.read("$v0")
                rs_rt = self.__short_circuit_unit.check_ex_mem(["$a0", "$v0"], [rt, rs])
                rt = rs_rt.get("$a0", None)
                rs = rs_rt.get("$v0", None)
                rs_rt = self.__short_circuit_unit.check_mem_wb(["$a0", "$v0"], [rt, rs])
                rt = rs_rt.get("$a0", None)
                rs = rs_rt.get("$v0", None)
                if rt is None or rs is None:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[ControlUnit]: Register '{'$a0' if rt is None else '$v0'}' "
                          f"provoked a bubble. {Style.RESET_ALL}")
                    return False, True
                self.__circuit.get_id_ex().write(if_id, new_rs=rs, new_rt=rt)
                return True, None
            cod_op = if_id.split()[0]
            if len(if_id.split()[1].split(',')) == 3:
                rd, rs, rt = if_id.split()[1].split(',')
                if cod_op == "addi":
                    rs_value = RegistersMemory.read(rs)
                    new_rs_value = (self.__short_circuit_unit.check_ex_mem([rs],
                                                                           [rs_value], "sw" if self.__circuit
                                                                           .get_id_ex().read_cod_op() == "sw" else None)
                                    .get(rs, None))
                    if new_rs_value is None:
                        new_rs_value = (self.__short_circuit_unit.check_mem_wb([rs],
                                                                               [new_rs_value], "sw" if self.__circuit
                                                                               .get_id_ex().read_cod_op() == "sw"
                                                                               else None)
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
                    rs_value, rt_value = RegistersMemory.read(rs), RegistersMemory.read(rt)
                    rs_rt_values = self.__short_circuit_unit.check_ex_mem([rs, rt],
                                                                          [rs_value, rt_value], "sw" if self.__circuit
                                                                          .get_aux_ex_mem().read_cod_op() == "sw" else None)
                    rs_value = rs_rt_values.get(rs, None)
                    rt_value = rs_rt_values.get(rt, None)
                    if rs_value is None:
                        rs_value = (self.__short_circuit_unit.check_mem_wb([rs],
                                                                           [rs_value], "sw" if self.__circuit
                                                                           .get_id_ex().get_aux_ex_mem() == "sw" else None)
                                    .get(rs, None))
                    if rt_value is None:
                        rt_value = (self.__short_circuit_unit.check_mem_wb([rt],
                                                                           [rt_value], "sw" if self.__circuit
                                                                           .get_id_ex().get_aux_ex_mem() == "sw" else None)
                        # TODO CHECK THIS
                                    .get(rt, None))
                    if rs_value is None or rt_value is None:
                        raise Exception(f"Instruction '{cod_op}' should not provoked a bubble. {Style.RESET_ALL}")
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs_value}', second operand "
                      f"'{rt_value}'")
                self.__circuit.get_id_ex().write(cod_op, rd, rs_value, rt_value)
                return True, None
                # instruction, destiny, op1, op2
            elif len(if_id.split()[1].split(',')) == 2:
                if cod_op == "sw":
                    rs, rd = if_id.split()[1].split(',')
                    rs_value = RegistersMemory.read(rs)
                    rs_value = (self.__short_circuit_unit.check_ex_mem([rs],
                                                                       [rs_value], "sw" if self.__circuit
                                                                       .get_id_ex().read_cod_op() == "sw" else None)
                                .get(rs, None))
                    if rs_value is None:
                        rs_value = (self.__short_circuit_unit.check_mem_wb([rs],
                                                                           [rs_value], "sw" if self.__circuit
                                                                           .get_id_ex().read_cod_op() == "sw" else None)
                                    .get(rs, None))
                    if rs_value is None:
                        print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                              f"[ControlUnit]: Register '{rs}' provoked a bubble. {Style.RESET_ALL}")
                        return False, True
                    mem_address, which_mem = LabelAddressMemory.read(rd)
                    if which_mem != 'D':
                        raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                        f"[ControlUnit]: Wrong memory access, aborting execution ...")
                    self.__circuit.get_id_ex().write(cod_op, mem_address, rs_value)
                    return True, None
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
                return True, None
            # TODO: Needs comparison of jump here
            # TODO: Calculate address to jump and put a print simulating in EX
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
            elif ex_mem.read_cod_op() == "la":
                mem_wb.write(ex_mem.read_destination(), DataMemory.read(ex_mem.read_address_or_value()))
                return True
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
                    inp = int(input(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    self.__circuit.get_aux_ex_mem().write(cod_op, "$v0", inp, True)
                    return True
                else:
                    raise Exception("SysCall wrong code ...")
                    # TODO missing SysCall code 1 implementation
            rd, rs, rt = id_ex.read_rd(), id_ex.read_rs(), id_ex.read_rt()
            if cod_op == "addi":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().add(int(rs), int(rt)), True)
                return True
            elif cod_op == "mul":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().multiply(int(rs), int(rt)), True)
                return True
            elif cod_op == "sub":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd,
                                                      self.__circuit.get_basic_alu().subtract(int(rs), int(rt)), True)
                return True
            elif cod_op == "li" or cod_op == "la" or cod_op == "sw":
                self.__circuit.get_aux_ex_mem().write(cod_op, rd, rs, True)
                return True
        return False

    def write_back(self, mem_wb):
        if mem_wb is not False:
            mem_wb = self.__circuit.get_mem_wb()
            RegistersMemory.write(mem_wb.read_destination(),
                                  mem_wb.read_address_or_value())
