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
from IntermediateRegisters import If_Id, Id_Ex, Ex_Mem, Mem_Wb


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
                return Id_Ex(if_id)
            cod_op = if_id.split()[0]
            if len(if_id.split()[1].split(',')) == 3:
                rd, rs, rt = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}', second operand "
                      f"'{rt}'")
                return Id_Ex(cod_op, rd, rs, rt)
                # instruction, destiny, op1, op2
            elif len(if_id.split()[1].split(',')) == 2:
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
                v0_value = RegistersMemory.read("$v0")
                # I/O operations
                if int(v0_value) == 4:
                    a0_value = RegistersMemory.read("$a0")
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Output]: {a0_value}{Style.RESET_ALL}")
                    return None
                    # TODO need to solve RAW between syscall and write_back
                else:
                    print(f"{Fore.YELLOW}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                          f"[SysCall/Input]: {Style.RESET_ALL}", end="")
                    inp = int(input(f"{Fore.YELLOW}{Style.BRIGHT}"))
                    print(f"{Style.RESET_ALL}", end="")
                    return Ex_Mem(cod_op, "$v0", inp)
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Executing '{cod_op}' instruction ...")
            if cod_op == "addi":
                rd, rs, rt = id_ex.read_rd(), id_ex.read_rs(), id_ex.read_rt()
                return Ex_Mem(cod_op, rd, ALU.add(int(RegistersMemory.read(rs)), int(rt)))
            elif cod_op == "li":
                return Ex_Mem(cod_op, id_ex.read_rd(), id_ex.read_rs())
            elif cod_op == "la":
                rd, rs = id_ex.read_rd(), id_ex.read_rs()
                mem_address, which_mem = LabelAddressMemory.read(rs)
                if which_mem == 'D':
                    return Ex_Mem(cod_op, rd, mem_address)
                else:
                    raise Exception(f"{datetime.now().strftime('[%H:%M:%S]')}"
                                    f"[ControlUnit]: Wrong memory access, aborting execution ...")
            elif cod_op == "sw":
                return Ex_Mem(cod_op, LabelAddressMemory.read(id_ex.read_rd()),
                              RegistersMemory.read(id_ex.read_rs()))
        return None

    @staticmethod
    def write_back(mem_wb):
        if mem_wb is not None:
            RegistersMemory.write(mem_wb.read_destination(), mem_wb.read_value())
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
        if_id, ex_mem, mem_wb, id_ex = [None]*4
        try:
            while True:
                Segmentation.write_back(mem_wb)
                aux = Segmentation.execute(id_ex)
                mem_wb = Segmentation.memory(ex_mem)
                ex_mem = aux
                id_ex = Segmentation.decode(if_id)
                if_id = Segmentation.fetch(PC.read())

                # If all the variables are empty, we break the loop
                if (if_id is None and ex_mem is None
                        and mem_wb is None and id_ex is None):
                    break
        except Exception as e:
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: {e} {Style.RESET_ALL}")
            print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Program exited with error code 1 {Style.RESET_ALL}")
            return
        print(f"{Fore.LIGHTGREEN_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Program exited with error code 0 {Style.RESET_ALL}")


if __name__ == '__main__':
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Generating Circuit ... {Style.RESET_ALL}")
    ControlUnit.interpret(sys.argv)
    print(f"{Fore.LIGHTBLUE_EX}{Style.BRIGHT}{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Starting program ... {Style.RESET_ALL}")
    ControlUnit.start()
