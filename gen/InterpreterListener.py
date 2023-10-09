# Generated from /Users/diegopicazo/Documents/github/MIPS32Simulator/Interpreter.g4 by ANTLR 4.13.1
from library.antlr4 import *
if "." in __name__:
    from .InterpreterParser import InterpreterParser
else:
    from InterpreterParser import InterpreterParser

# This class defines a complete listener for a parse tree produced by InterpreterParser.
class InterpreterListener(ParseTreeListener):

    # Enter a parse tree produced by InterpreterParser#data.
    def enterData(self, ctx:InterpreterParser.DataContext):
        pass

    # Exit a parse tree produced by InterpreterParser#data.
    def exitData(self, ctx:InterpreterParser.DataContext):
        pass


    # Enter a parse tree produced by InterpreterParser#data_block.
    def enterData_block(self, ctx:InterpreterParser.Data_blockContext):
        pass

    # Exit a parse tree produced by InterpreterParser#data_block.
    def exitData_block(self, ctx:InterpreterParser.Data_blockContext):
        pass


    # Enter a parse tree produced by InterpreterParser#instruction.
    def enterInstruction(self, ctx:InterpreterParser.InstructionContext):
        pass

    # Exit a parse tree produced by InterpreterParser#instruction.
    def exitInstruction(self, ctx:InterpreterParser.InstructionContext):
        pass


    # Enter a parse tree produced by InterpreterParser#instruction_block.
    def enterInstruction_block(self, ctx:InterpreterParser.Instruction_blockContext):
        pass

    # Exit a parse tree produced by InterpreterParser#instruction_block.
    def exitInstruction_block(self, ctx:InterpreterParser.Instruction_blockContext):
        pass


    # Enter a parse tree produced by InterpreterParser#interpret.
    def enterInterpret(self, ctx:InterpreterParser.InterpretContext):
        pass

    # Exit a parse tree produced by InterpreterParser#interpret.
    def exitInterpret(self, ctx:InterpreterParser.InterpretContext):
        pass



del InterpreterParser