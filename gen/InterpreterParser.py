# Generated from /Users/diegopicazo/Documents/github/MIPS32Simulator/Interpreter.g4 by ANTLR 4.13.1
# encoding: utf-8
from library.antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


from Circuit import Circuit

def serializedATN():
    return [
        4,1,13,84,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,1,0,3,0,13,
        8,0,1,0,1,0,1,0,1,0,1,0,1,0,3,0,21,8,0,1,0,1,0,1,1,1,1,3,1,27,8,
        1,1,1,1,1,3,1,31,8,1,1,1,5,1,34,8,1,10,1,12,1,37,9,1,1,1,3,1,40,
        8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,3,3,50,8,3,1,3,1,3,1,3,3,3,55,
        8,3,1,3,5,3,58,8,3,10,3,12,3,61,9,3,1,3,3,3,64,8,3,1,3,1,3,1,4,1,
        4,3,4,70,8,4,1,4,1,4,1,4,4,4,75,8,4,11,4,12,4,76,1,4,1,4,1,4,3,4,
        82,8,4,1,4,0,0,5,0,2,4,6,8,0,1,1,0,10,13,91,0,10,1,0,0,0,2,24,1,
        0,0,0,4,43,1,0,0,0,6,47,1,0,0,0,8,81,1,0,0,0,10,12,5,7,0,0,11,13,
        5,5,0,0,12,11,1,0,0,0,12,13,1,0,0,0,13,20,1,0,0,0,14,15,5,1,0,0,
        15,16,5,8,0,0,16,21,6,0,-1,0,17,18,5,2,0,0,18,19,5,9,0,0,19,21,6,
        0,-1,0,20,14,1,0,0,0,20,17,1,0,0,0,21,22,1,0,0,0,22,23,6,0,-1,0,
        23,1,1,0,0,0,24,26,5,3,0,0,25,27,5,5,0,0,26,25,1,0,0,0,26,27,1,0,
        0,0,27,28,1,0,0,0,28,35,3,0,0,0,29,31,5,5,0,0,30,29,1,0,0,0,30,31,
        1,0,0,0,31,32,1,0,0,0,32,34,3,0,0,0,33,30,1,0,0,0,34,37,1,0,0,0,
        35,33,1,0,0,0,35,36,1,0,0,0,36,39,1,0,0,0,37,35,1,0,0,0,38,40,5,
        5,0,0,39,38,1,0,0,0,39,40,1,0,0,0,40,41,1,0,0,0,41,42,6,1,-1,0,42,
        3,1,0,0,0,43,44,7,0,0,0,44,45,6,2,-1,0,45,46,6,2,-1,0,46,5,1,0,0,
        0,47,49,5,7,0,0,48,50,5,5,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,51,
        1,0,0,0,51,52,3,4,2,0,52,59,6,3,-1,0,53,55,5,5,0,0,54,53,1,0,0,0,
        54,55,1,0,0,0,55,56,1,0,0,0,56,58,3,4,2,0,57,54,1,0,0,0,58,61,1,
        0,0,0,59,57,1,0,0,0,59,60,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,62,
        64,5,5,0,0,63,62,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,6,3,-1,
        0,66,7,1,0,0,0,67,69,6,4,-1,0,68,70,3,2,1,0,69,68,1,0,0,0,69,70,
        1,0,0,0,70,71,1,0,0,0,71,72,5,4,0,0,72,74,6,4,-1,0,73,75,3,6,3,0,
        74,73,1,0,0,0,75,76,1,0,0,0,76,74,1,0,0,0,76,77,1,0,0,0,77,78,1,
        0,0,0,78,79,6,4,-1,0,79,82,1,0,0,0,80,82,5,6,0,0,81,67,1,0,0,0,81,
        80,1,0,0,0,82,9,1,0,0,0,13,12,20,26,30,35,39,49,54,59,63,69,76,81
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, circuit=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.circuit = None
            self.new_circuit = None
            self._TAG = None # Token
            self._STRING = None # Token
            self._INTEGER = None # Token
            self.circuit = circuit

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




    def data(self, circuit):

        localctx = InterpreterParser.DataContext(self, self._ctx, self.state, circuit)
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

                generated_address = localctx.circuit.get_data_memory().generate_address()
                localctx.circuit.get_data_memory().write(generated_address, (None if localctx._STRING is None else localctx._STRING.text))
                localctx.circuit.get_label_address_memory().write((None if localctx._TAG is None else localctx._TAG.text).replace(':', ''), (generated_address, 'D'))

                pass
            elif token in [2]:
                self.state = 17
                self.match(InterpreterParser.T__1)
                self.state = 18
                localctx._INTEGER = self.match(InterpreterParser.INTEGER)

                generated_address = localctx.circuit.get_data_memory().generate_address()
                localctx.circuit.get_data_memory().write(localctx.circuit.get_data_memory().generate_address(),
                        int((None if localctx._INTEGER is None else localctx._INTEGER.text)))
                localctx.circuit.get_label_address_memory().write((None if localctx._TAG is None else localctx._TAG.text).replace(':', ''), (generated_address, 'D'))

                pass
            else:
                raise NoViableAltException(self)

            localctx.new_circuit = localctx.circuit
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Data_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, circuit=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.circuit = None
            self.new_circuit = None
            self._data = None # DataContext
            self.circuit = circuit

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




    def data_block(self, circuit):

        localctx = InterpreterParser.Data_blockContext(self, self._ctx, self.state, circuit)
        self.enterRule(localctx, 2, self.RULE_data_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 24
            self.match(InterpreterParser.T__2)
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 25
                self.match(InterpreterParser.WS)


            self.state = 28
            localctx._data = self.data(localctx.circuit)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 30
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 29
                        self.match(InterpreterParser.WS)


                    self.state = 32
                    localctx._data = self.data(localctx.circuit) 
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

            self.state = 39
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 38
                self.match(InterpreterParser.WS)



            localctx.new_circuit = localctx._data.new_circuit

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InstructionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, circuit=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.circuit = None
            self.generated_address = None
            self.new_circuit = None
            self.circuit = circuit

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




    def instruction(self, circuit):

        localctx = InterpreterParser.InstructionContext(self, self._ctx, self.state, circuit)
        self.enterRule(localctx, 4, self.RULE_instruction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15360) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()

            generated_address = localctx.circuit.get_instruction_memory().generate_address()
            localctx.circuit.get_instruction_memory().write(generated_address, self._input.getText(localctx.start, self._input.LT(-1)).replace('\t', '    '))
            localctx.generated_address = generated_address

            localctx.new_circuit = localctx.circuit
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Instruction_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1, circuit=None):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.circuit = None
            self.new_circuit = None
            self._TAG = None # Token
            self._instruction = None # InstructionContext
            self.circuit = circuit

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




    def instruction_block(self, circuit):

        localctx = InterpreterParser.Instruction_blockContext(self, self._ctx, self.state, circuit)
        self.enterRule(localctx, 6, self.RULE_instruction_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            localctx._TAG = self.match(InterpreterParser.TAG)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 48
                self.match(InterpreterParser.WS)


            self.state = 51
            localctx._instruction = self.instruction(localctx.circuit)

            localctx._instruction.new_circuit.get_label_address_memory().write((None if localctx._TAG is None else localctx._TAG.text).replace(':', ''), (localctx._instruction.generated_address, 'I'))

            self.state = 59
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 54
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==5:
                        self.state = 53
                        self.match(InterpreterParser.WS)


                    self.state = 56
                    localctx._instruction = self.instruction(localctx.circuit) 
                self.state = 61
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 62
                self.match(InterpreterParser.WS)



            localctx.new_circuit = localctx._instruction.new_circuit

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
            self.circuit = None
            self._data_block = None # Data_blockContext
            self._instruction_block = None # Instruction_blockContext

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
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [3, 4]:
                self.enterOuterAlt(localctx, 1)

                localctx.circuit =  Circuit()

                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==3:
                    self.state = 68
                    localctx._data_block = self.data_block(localctx.circuit)


                self.state = 71
                self.match(InterpreterParser.T__3)
                localctx.circuit = localctx._data_block.new_circuit
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 73
                    localctx._instruction_block = self.instruction_block(localctx.circuit)
                    self.state = 76 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break


                localctx.circuit = localctx._instruction_block.new_circuit

                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 2)
                self.state = 80
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





