import sys
import time

from datetime import datetime
from gen.InterpreterLexer import InterpreterLexer
from gen.InterpreterParser import InterpreterParser
from library.antlr4 import *
from io import StringIO
from library.colorama import Fore, Style
from Control.Segmentation import Segmentation
from Control.ForwardingUnit import ForwardingUnit
from Circuit import Circuit


class ControlUnit:

    def __init__(self):
        self.__circuit = Circuit()
        self.__segmentation = Segmentation(self.__circuit,
                                           ForwardingUnit(self.__circuit))

    # Used only once at the beginning to override the empty Circuit with the one which has read data
    def override_circuit(self, circuit):
        self.__circuit = circuit
        self.__segmentation = Segmentation(circuit, ForwardingUnit(circuit))

    def interpret(self, argv):
        time.sleep(0.2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[Interpreter]: Reading input file ({argv[1]}) ...")
        # Save the original stderr and redirects the actual one into a stream
        original_stderr = sys.stderr
        compilation_errors_stream = StringIO()
        sys.stderr = compilation_errors_stream
        # Interpret the file to load the circuit
        interpret_context = InterpreterParser(
            CommonTokenStream(
                InterpreterLexer(
                    FileStream(argv[1])))).interpret()
        time.sleep(0.2)
        # Establish the stderr to default
        sys.stderr = original_stderr
        # Check if there were any interpreted errors
        if compilation_errors_stream.getvalue():
            error_messages = (compilation_errors_stream.getvalue()
                              .strip().split('\n'))
            for err_msg in error_messages:
                print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Interpreter]: {err_msg}")
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[Interpreter]: Failed to read input file ({argv[1]}).")
            compilation_errors_stream.close()
            exit(1)
        # Otherwise we fill the memories and start the circuit
        else:
            compilation_errors_stream.close()
            time.sleep(0.2)
            print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Printing Memories ... ")
            time.sleep(0.1)
            # Overrides circuit from interpreter context to control unit class
            self.override_circuit(interpret_context.circuit)
            print()
            self.__circuit.get_data_memory().print()
            self.__circuit.get_instruction_memory().print()
            self.__circuit.get_label_address_memory().print()
            print(f"{Style.RESET_ALL}")

    def start(self):
        if_id, mem_wb, ex_mem, id_ex = [False] * 4
        i = 0
        try:
            while True:
                print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                      f"{'-'*45} ITERATION {i} {'-'*45}{Style.RESET_ALL}")
                i = i + 1
                self.__segmentation.write_back(mem_wb)
                aux = self.__segmentation.execute(id_ex)
                mem_wb = self.__segmentation.memory(ex_mem)
                # Need due to tunneling memory between EX and MEM phase
                ex_mem = aux
                if ex_mem is not False:
                    self.__circuit.get_ex_mem().write(self.__circuit.get_aux_ex_mem().read_cod_op(),
                                                      self.__circuit.get_aux_ex_mem().read_destination(),
                                                      self.__circuit.get_aux_ex_mem().read_address_or_value(True))
                else:
                    self.__circuit.get_ex_mem().clear()
                id_ex, exists_bubble = self.__segmentation.decode(if_id)
                if exists_bubble is True:
                    continue
                if_id = self.__segmentation.fetch()
                # If all the variables are empty, we break the loop
                if (if_id is False and ex_mem is False
                        and mem_wb is False and id_ex is False):
                    break
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: {e} {Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Program exited with error code 1 {Style.RESET_ALL}")
            return
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Program exited with error code 0 {Style.RESET_ALL}")
