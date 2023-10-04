# Generated from /Users/diegopicazo/Downloads/practica2/Interpreter.g4 by ANTLR 4.13.1
# encoding: utf-8
from library.antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from InstructionMemory import InstructionMemory
from DataMemory import DataMemory
from LabelAddressMemory import LabelAddressMemory

def serializedATN():
    return [
        4,1,13,73,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,1,1,1,3,1,25,8,1,1,1,1,
        1,3,1,29,8,1,1,1,5,1,32,8,1,10,1,12,1,35,9,1,1,1,3,1,38,8,1,1,2,
        1,2,1,2,1,3,1,3,3,3,45,8,3,1,3,1,3,1,3,3,3,50,8,3,1,3,5,3,53,8,3,
        10,3,12,3,56,9,3,1,3,3,3,59,8,3,1,4,3,4,62,8,4,1,4,1,4,4,4,66,8,
        4,11,4,12,4,67,1,4,3,4,71,8,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,10,13,
        80,0,10,1,0,0,0,2,22,1,0,0,0,4,39,1,0,0,0,6,42,1,0,0,0,8,70,1,0,
        0,0,10,12,5,7,0,0,11,13,5,5,0,0,12,11,1,0,0,0,12,13,1,0,0,0,13,20,
        1,0,0,0,14,15,5,1,0,0,15,16,5,8,0,0,16,21,6,0,-1,0,17,18,5,2,0,0,
        18,19,5,9,0,0,19,21,6,0,-1,0,20,14,1,0,0,0,20,17,1,0,0,0,21,1,1,
        0,0,0,22,24,5,3,0,0,23,25,5,5,0,0,24,23,1,0,0,0,24,25,1,0,0,0,25,
        26,1,0,0,0,26,33,3,0,0,0,27,29,5,5,0,0,28,27,1,0,0,0,28,29,1,0,0,
        0,29,30,1,0,0,0,30,32,3,0,0,0,31,28,1,0,0,0,32,35,1,0,0,0,33,31,
        1,0,0,0,33,34,1,0,0,0,34,37,1,0,0,0,35,33,1,0,0,0,36,38,5,5,0,0,
        37,36,1,0,0,0,37,38,1,0,0,0,38,3,1,0,0,0,39,40,7,0,0,0,40,41,6,2,
        -1,0,41,5,1,0,0,0,42,44,5,7,0,0,43,45,5,5,0,0,44,43,1,0,0,0,44,45,
        1,0,0,0,45,46,1,0,0,0,46,47,3,4,2,0,47,54,6,3,-1,0,48,50,5,5,0,0,
        49,48,1,0,0,0,49,50,1,0,0,0,50,51,1,0,0,0,51,53,3,4,2,0,52,49,1,
        0,0,0,53,56,1,0,0,0,54,52,1,0,0,0,54,55,1,0,0,0,55,58,1,0,0,0,56,
        54,1,0,0,0,57,59,5,5,0,0,58,57,1,0,0,0,58,59,1,0,0,0,59,7,1,0,0,
        0,60,62,3,2,1,0,61,60,1,0,0,0,61,62,1,0,0,0,62,63,1,0,0,0,63,65,
        5,4,0,0,64,66,3,6,3,0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,
        67,68,1,0,0,0,68,71,1,0,0,0,69,71,5,6,0,0,70,61,1,0,0,0,70,69,1,
        0,0,0,71,9,1,0,0,0,13,12,20,24,28,33,37,44,49,54,58,61,67,70
    ]

class InterpreterParser ( Parser ):

    grammarFileName = "Interpreter.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.asciiz'", "'.word'", "'.data'", "'.text'", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'syscall'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "WS", "COMMENT", "TAG", "STRING", "INTEGER", 
                      "SYSCALL", "R_OPERATION", "I_OPERATION", "J_OPERATION" ]

    RULE_data = 0
    RULE_data_block = 1
    RULE_instruction = 2
    RULE_instruction_block = 3
    RULE_interpret = 4

    ruleNames =  [ "data", "data_block", "instruction", "instruction_block", 
                   "interpret" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    WS=5
    COMMENT=6
    TAG=7
    STRING=8
    INTEGER=9
    SYSCALL=10
    R_OPERATION=11
    I_OPERATION=12
    J_OPERATION=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class DataContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TAG = None # Token
            self._STRING = None # Token
            self._INTEGER = None # Token

        def TAG(self):
            return self.getToken(InterpreterParser.TAG, 0)

        def STRING(self):
            return self.getToken(InterpreterParser.STRING, 0)

        def INTEGER(self):
            return self.getToken(InterpreterParser.INTEGER, 0)

        def WS(self):
            return self.getToken(InterpreterParser.WS, 0)

        def getRuleIndex(self):
            return InterpreterParser.RULE_data

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData" ):
                listener.enterData(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData" ):
                listener.exitData(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData" ):
                return visitor.visitData(self)
            else:
                return visitor.visitChildren(self)




    def data(self):

        localctx = InterpreterParser.DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_data)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 10
            localctx._TAG = self.match(InterpreterParser.TAG)
            self.state = 12
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 11
                self.match(InterpreterParser.WS)


            self.state = 20
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 14
                self.match(InterpreterParser.T__0)
                self.state = 15
                localctx._STRING = self.match(InterpreterParser.STRING)

                generated_address = DataMemory.generate_address()
                DataMemory.write(generated_address, (None if localctx._STRING is None else localctx._STRING.text))
                LabelAddressMemory.write((None if localctx._TAG is None else localctx._TAG.text), (generated_address, 'D'))

                pass
            elif token in [2]:
                self.state = 17
                self.match(InterpreterParser.T__1)
                self.state = 18
                localctx._INTEGER = self.match(InterpreterParser.INTEGER)

                generated_address = DataMemory.generate_address()
                DataMemory.write(DataMemory.generate_address(),
                        int((None if localctx._INTEGER is None else localctx._INTEGER.text)))
                LabelAddressMemory.write((None if localctx._TAG is None else localctx._TAG.text), (generated_address, 'D'))

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.DataContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.DataContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(InterpreterParser.WS)
            else:
                return self.getToken(InterpreterParser.WS, i)

        def getRuleIndex(self):
            return InterpreterParser.RULE_data_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_block" ):
                listener.enterData_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_block" ):
                listener.exitData_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitData_block" ):
                return visitor.visitData_block(self)
            else:
                return visitor.visitChildren(self)




    def data_block(self):

        localctx = InterpreterParser.Data_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_data_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(InterpreterParser.T__2)
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 23
                self.match(InterpreterParser.WS)


            self.state = 26
            self.data()
            self.state = 33
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 28
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 27
                        self.match(InterpreterParser.WS)


                    self.state = 30
                    self.data() 
                self.state = 35
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 36
                self.match(InterpreterParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.generated_address = None

        def SYSCALL(self):
            return self.getToken(InterpreterParser.SYSCALL, 0)

        def R_OPERATION(self):
            return self.getToken(InterpreterParser.R_OPERATION, 0)

        def I_OPERATION(self):
            return self.getToken(InterpreterParser.I_OPERATION, 0)

        def J_OPERATION(self):
            return self.getToken(InterpreterParser.J_OPERATION, 0)

        def getRuleIndex(self):
            return InterpreterParser.RULE_instruction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction" ):
                listener.enterInstruction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction" ):
                listener.exitInstruction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction" ):
                return visitor.visitInstruction(self)
            else:
                return visitor.visitChildren(self)




    def instruction(self):

        localctx = InterpreterParser.InstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            generated_address = InstructionMemory.generate_address()
            InstructionMemory.write(generated_address, self._input.getText(localctx.start, self._input.LT(-1)).replace('\t', '    '))
            localctx.generated_address = generated_address

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self._TAG = None # Token
            self._instruction = None # InstructionContext

        def TAG(self):
            return self.getToken(InterpreterParser.TAG, 0)

        def instruction(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.InstructionContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.InstructionContext,i)


        def WS(self, i:int=None):
            if i is None:
                return self.getTokens(InterpreterParser.WS)
            else:
                return self.getToken(InterpreterParser.WS, i)

        def getRuleIndex(self):
            return InterpreterParser.RULE_instruction_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInstruction_block" ):
                listener.enterInstruction_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInstruction_block" ):
                listener.exitInstruction_block(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInstruction_block" ):
                return visitor.visitInstruction_block(self)
            else:
                return visitor.visitChildren(self)




    def instruction_block(self):

        localctx = InterpreterParser.Instruction_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_instruction_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            localctx._TAG = self.match(InterpreterParser.TAG)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 43
                self.match(InterpreterParser.WS)


            self.state = 46
            localctx._instruction = self.instruction()

            LabelAddressMemory.write((None if localctx._TAG is None else localctx._TAG.text), (localctx._instruction.generated_address, 'I'))

            self.state = 54
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 49
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 48
                        self.match(InterpreterParser.WS)


                    self.state = 51
                    localctx._instruction = self.instruction() 
                self.state = 56
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 57
                self.match(InterpreterParser.WS)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterpretContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_block(self):
            return self.getTypedRuleContext(InterpreterParser.Data_blockContext,0)


        def instruction_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(InterpreterParser.Instruction_blockContext)
            else:
                return self.getTypedRuleContext(InterpreterParser.Instruction_blockContext,i)


        def COMMENT(self):
            return self.getToken(InterpreterParser.COMMENT, 0)

        def getRuleIndex(self):
            return InterpreterParser.RULE_interpret

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInterpret" ):
                listener.enterInterpret(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInterpret" ):
                listener.exitInterpret(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterpret" ):
                return visitor.visitInterpret(self)
            else:
                return visitor.visitChildren(self)




    def interpret(self):

        localctx = InterpreterParser.InterpretContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_interpret)
        self._la = 0 # Token type
        try:
            self.state = 70
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 60
                    self.data_block()


                self.state = 63
                self.match(InterpreterParser.T__3)
                self.state = 65 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 64
                    self.instruction_block()
                    self.state = 67 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(InterpreterParser.COMMENT)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





