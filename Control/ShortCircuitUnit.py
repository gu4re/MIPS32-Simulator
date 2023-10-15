from Circuit import Circuit
from Memory.RegistersMemory import RegistersMemory
from datetime import datetime
from library.colorama import Fore, Style


class ShortCircuitUnit:

    def __init__(self, circuit: Circuit):
        self.__circuit = circuit

    @staticmethod
    def __check(memory, registers_on_read):
        new_registers_on_read = {}
        memory = memory
        for register in registers_on_read:
            if register == memory.read_destination():
                print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[ShortCircuitUnit]: Register '{register}' provoked a short-circuit. {Style.RESET_ALL}")
                new_registers_on_read[register] = memory.read_address_or_value()
            else:
                new_registers_on_read[register] = RegistersMemory.read(register)
        return new_registers_on_read

    def check_ex_mem(self, registers_on_read: list):
        return self.__check(self.__circuit.get_ex_mem(), registers_on_read)

    def check_mem_wb(self, registers_on_read: list):
        return self.__check(self.__circuit.get_mem_wb(), registers_on_read)
