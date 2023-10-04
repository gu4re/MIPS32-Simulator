# Generated from /Users/diegopicazo/Downloads/practica2/Interpreter.g4 by ANTLR 4.13.1
from library.antlr4 import *
if "." in __name__:
    from .InterpreterParser import InterpreterParser
else:
    from InterpreterParser import InterpreterParser

# This class defines a complete generic visitor for a parse tree produced by InterpreterParser.

class InterpreterVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by InterpreterParser#data.
    def visitData(self, ctx:InterpreterParser.DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#data_block.
    def visitData_block(self, ctx:InterpreterParser.Data_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#instruction.
    def visitInstruction(self, ctx:InterpreterParser.InstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#instruction_block.
    def visitInstruction_block(self, ctx:InterpreterParser.Instruction_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by InterpreterParser#interpret.
    def visitInterpret(self, ctx:InterpreterParser.InterpretContext):
        return self.visitChildren(ctx)



del InterpreterParser