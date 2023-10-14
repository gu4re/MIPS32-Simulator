import sys
import time

from datetime import datetime
from gen.InterpreterLexer import InterpreterLexer
from gen.InterpreterParser import InterpreterParser
from library.antlr4 import *
from io import StringIO
from Memory.DataMemory import DataMemory
from Memory.InstructionMemory import InstructionMemory
from Memory.LabelAddressMemory import LabelAddressMemory
from library.colorama import Fore, Style
from Control.Segmentation import Segmentation
from Control.ShortCircuitUnit import ShortCircuitUnit
from Circuit import Circuit

# TODO Needs Forwarding unit class to solve RAWs
# TODO Needs a Circuit Class to group all elements to solve RAWs


class ControlUnit:

    def __init__(self):
        self.__circuit = Circuit()
        self.__segmentation = Segmentation(self.__circuit)
        self.__short_circuit_unit = ShortCircuitUnit(self.__circuit)

    @staticmethod
    def interpret(argv):
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[Interpreter]: Reading input file ({argv[1]}) ...")
        # Save the original stderr and redirects the actual one into a stream
        original_stderr = sys.stderr
        compilation_errors_stream = StringIO()
        sys.stderr = compilation_errors_stream
        # Interpret the file
        InterpreterParser(
            CommonTokenStream(
                InterpreterLexer(
                    FileStream(argv[1])))).interpret()
        # TODO should abstract Interpreter to another class
        time.sleep(2)
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
            time.sleep(2)
            print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Printing Memories ... ")
            time.sleep(1)
            print()
            DataMemory.print()
            InstructionMemory.print()
            LabelAddressMemory.print()
            print(f"{Style.RESET_ALL}")

    def start(self):
        if_id, mem_wb, ex_mem, id_ex = [False] * 4
        i = 0
        try:
            while True:
                print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                      f"{'-'*45} PHASE {i} {'-'*45}{Style.RESET_ALL}")
                self.__segmentation.write_back(mem_wb)
                aux = Segmentation.execute(id_ex)
                mem_wb = self.__segmentation.memory(ex_mem)
                ex_mem = aux
                id_ex = self.__segmentation.decode(if_id)
                if_id = self.__segmentation.fetch()
                i = i + 1
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
