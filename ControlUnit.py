import sys
import time

from datetime import datetime
from gen.InterpreterLexer import InterpreterLexer
from gen.InterpreterParser import InterpreterParser
from library.antlr4 import *
from io import StringIO
from DataMemory import DataMemory
from InstructionMemory import InstructionMemory
from LabelAddressMemory import LabelAddressMemory
from RegistersMemory import RegistersMemory
from PC import PC
from ALU import ALU
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
        return instruction

    @staticmethod
    def decode(if_id):
        if if_id is not None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction '{if_id}' ...")
            # Syscall path
            if if_id == "syscall":
                return if_id
            cod_op = if_id.split()[0]
            if len(if_id.split()[1].split(',')) == 3:
                rd, rs, rt = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}', second operand "
                      f"'{rt}'")
                return cod_op, rd, rs, rt
                # instruction, destiny, op1, op2
            elif len(if_id.split()[1].split(',')) == 2:
                rd, rs = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}'")
                return cod_op, rd, rs
            # TODO: Needs comparison of jump here
        return None

    @staticmethod
    def memory(exec_mem):
        if exec_mem is not None:
            address, value = exec_mem
        # TODO: Needs implementation
        return None

    @staticmethod
    def execute(dec_exec):
        if dec_exec is not None:
            if dec_exec == "syscall":
                v0_value = RegistersMemory.read("$v0")
                # I/O operations
                if int(v0_value) == 4:
                    a0_value = RegistersMemory.read("$a0")
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Output]: {a0_value}{Style.RESET_ALL}")
                    return None
                else:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Input]: {Style.RESET_ALL}", end="")
                    inp = int(input(f"{Fore.YELLOW}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    RegistersMemory.write("$v0", inp)
                    return None
            cod_op = dec_exec[0]
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Executing '{cod_op}' instruction ...")
            if cod_op == "addi":
                rd, rs, rt = dec_exec[1:]
                RegistersMemory.write(rd, ALU.add(int(RegistersMemory.read(rs)),
                                                  int(rt)))
                return None
            elif cod_op == "li":
                rd, rs = dec_exec[1:]
                RegistersMemory.write(rd, rs)
                # Check if 'li' writes in EX time or WB time
                return None
            elif cod_op == "la":
                rd, rs = dec_exec[1:]
                mem_address, which_mem = LabelAddressMemory.read(rs)
                if which_mem == 'D':
                    RegistersMemory.write(rd, DataMemory.read(mem_address))
                    # Check if we read from dataMemory here or in MEM
                else:
                    raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                    f"[ControlUnit]: Wrong memory access, aborting execution ...")
            elif cod_op == "sw":
                rd, rs = dec_exec[1:]
                return LabelAddressMemory.read(rs), RegistersMemory.read(rd)
                # TODO missing implementation of sw
        return None

    @staticmethod
    def write_back(mem_wb):
        if mem_wb is not None:
            return None
        # TODO: Needs implementation
        return None


class ControlUnit:

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

    @staticmethod
    def start():
        if_id, exec_mem, mem_wb, dec_exec = [None]*4
        try:
            while True:
                Segmentation.write_back(mem_wb)
                aux = Segmentation.execute(dec_exec)
                mem_wb = Segmentation.memory(exec_mem)
                exec_mem = aux
                dec_exec = Segmentation.decode(if_id)
                if_id = Segmentation.fetch(PC.read())

                # If all the variables are empty, we break the loop
                if (if_id is None and exec_mem is None
                        and mem_wb is None and dec_exec is None):
                    break
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: {e} {Style.RESET_ALL}")
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Program exited with error code 0 {Style.RESET_ALL}")


if __name__ == '__main__':
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Generating Circuit ... {Style.RESET_ALL}")
    ControlUnit.interpret(sys.argv)
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Starting program ... {Style.RESET_ALL}")
    ControlUnit.start()
