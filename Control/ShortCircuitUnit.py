from Circuit import Circuit
from datetime import datetime
from library.colorama import Fore, Style


class ShortCircuitUnit:

    def __init__(self, circuit: Circuit):
        self.__circuit = circuit

    @staticmethod
    def __check(memory, registers_on_read, actual_values):
        new_registers_on_read = {}
        mem = memory
        i = 0
        for register in registers_on_read:
            if register == mem.read_destination():
                print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[ShortCircuitUnit]: Register '{register}' provoked a short-circuit in "
                      f"{type(mem).__name__.upper()}. {Style.RESET_ALL}")
                address_or_value = mem.read_address_or_value()
                if str(address_or_value).startswith("0x"):
                    new_registers_on_read[register] = None
                else:
                    new_registers_on_read[register] = address_or_value
            else:
                new_registers_on_read[register] = actual_values[i]
            i = i + 1
        return new_registers_on_read

    def check_ex_mem(self, registers_on_read: list, actual_values: list):
        return self.__check(self.__circuit.get_ex_mem(), registers_on_read, actual_values)

    def check_mem_wb(self, registers_on_read: list, actual_values: list):
        return self.__check(self.__circuit.get_mem_wb(), registers_on_read, actual_values)
