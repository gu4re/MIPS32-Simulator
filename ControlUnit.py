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


class Segmentation:

    @staticmethod
    def fetch(pc):
        print(f"{datetime.now().strftime('[%H:%M:%S]')}[ControlUnit]:"
              f" Fetching PC...")
        time.sleep(2)
        instruction = InstructionMemory.read(pc)
        if instruction is None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: No more instructions left!")
            return None
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Instruction read is '{instruction}'")
        time.sleep(2)
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[PC]: Updated!")
        PC.update(pc)
        return instruction

    @staticmethod
    def decode(if_id):
        if if_id is not None:
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Decoding instruction...")
            time.sleep(2)
            cod_op = if_id.split()[0]
            if len(if_id.split()[1].split(',')) == 3:
                rd, rs, rt = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}', second operand "
                      f"'{rt}'")
                time.sleep(2)
                return cod_op, rd, rs, rt
            else:
                rd, rs = if_id.split()[1].split(',')
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Decoder]: Operation code '{cod_op}', register of "
                      f"destiny '{rd}', first operand '{rs}'")
                time.sleep(2)
                return cod_op, rd, rs
                # instruction, destiny, op1, op2
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
            cod_op = dec_exec[0]
            if cod_op == "addi":
                rd, rs, rt = dec_exec[1:]
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[ControlUnit]: Executing 'addi' instruction ...")
                time.sleep(2)
                RegistersMemory.write(rd, ALU.add(RegistersMemory.read(rs),
                                                  int(rt)))
                return None
            elif cod_op == "li":
                rd, rs = dec_exec[1:]
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[ControlUnit]: Executing 'li' instruction ...")
                RegistersMemory.write(rd, rs)
                # Check if 'li' writes in EX time or WB time
                return None
            elif cod_op == "sw":
                rd, rs = dec_exec[1:]
                return LabelAddressMemory.read(rs), RegistersMemory.read(rd)
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
        time.sleep(2)
        # Establish the stderr to default
        sys.stderr = original_stderr
        # Check if there were any interpreted errors
        if compilation_errors_stream.getvalue():
            error_messages = (compilation_errors_stream.getvalue()
                              .strip().split('\n'))
            for err_msg in error_messages:
                print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                      f"[Interpreter]: {err_msg}")
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[Interpreter]: Failed to read input file ({argv[1]}).")
            compilation_errors_stream.close()
            exit(1)
        # Otherwise we fill the memories and start the circuit
        else:
            compilation_errors_stream.close()
            time.sleep(2)
            print(f"{datetime.now().strftime('[%H:%M:%S]')}"
                  f"[ControlUnit]: Filling Memories ... ")
            print()
            time.sleep(2)
            DataMemory.print()
            time.sleep(2)
            InstructionMemory.print()
            time.sleep(2)
            LabelAddressMemory.print()
            print()

    @staticmethod
    def start():
        if_id = None
        exec_mem = None
        mem_wb = None
        dec_exec = None
        
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
        print(f"{datetime.now().strftime('[%H:%M:%S]')}"
              f"[ControlUnit]: Finishing program ... ")


if __name__ == '__main__':
    print(f"{datetime.now().strftime('[%H:%M:%S]')}"
          f"[ControlUnit]: Generating Circuit ... ")
    time.sleep(2)
    ControlUnit.interpret(sys.argv)
    ControlUnit.start()