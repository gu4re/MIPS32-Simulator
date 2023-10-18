grammar Interpreter;

/********* Imports *********/
@parser::header {
from Memory.InstructionMemory import InstructionMemory
from Memory.DataMemory import DataMemory
from Memory.LabelAddressMemory import LabelAddressMemory
}

/********* Utilities *********/
WS: [ \t\r\n]+ -> skip; // Ignore tabs, spaces, and more
COMMENT: '#' ~[\r\n]* WS? -> skip; // Skip comments
TAG: [a-zA-Z0-9]+':' ;
STRING: '"' ( ~["] | '\\"' | WS)* '"' ;
INTEGER: [0-9]+ ;

/********* System Operations *********/
SYSCALL: 'syscall' ;

/********* R Operations *********/
fragment MUL:   'mul' WS '$'[atv][0-9]','WS*'$'[atv][0-9]','WS*'$'[atv][0-9] ;
fragment SUB:   'sub' WS '$'[atv][0-9]','WS*'$'[atv][0-9]','WS*'$'[atv][0-9] ;
fragment ADDI:  'addi' WS '$'[atv][0-9]','WS*'$'[atv][0-9]','WS*[0-9]+ ;
fragment ADD:   'add' WS '$'[atv][0-9]','WS*'$'[atv][0-9]','WS*'$'[atv][0-9] ;

R_OPERATION: MUL | SUB | ADDI | ADD ;

/********* I Operations *********/
fragment BGE:   'bge' WS '$'[atv][0-9]','WS*'$'[atv][0-9]','WS*[a-zA-Z0-9]+ ;
fragment LI:    'li' WS '$'[atv][0-9]',' WS* [0-9]+ ;
fragment LA:    'la' WS '$'[atv][0-9]','WS*[a-zA-Z0-9]+ ;
fragment LW:    'lw' WS '$'[atv][0-9]','WS*[a-zA-Z0-9]+ ;
fragment SW:    'sw' WS '$'[atv][0-9]','WS*[a-zA-Z0-9]+ ;

I_OPERATION: BGE | LI | LA | LW | SW ;

/********* J Operations *********/
J_OPERATION: 'j' WS [A-Za-z]+ ;

/********* Rules *********/
data: TAG WS? ('.asciiz' STRING {
generated_address = DataMemory.generate_address()
DataMemory.write(generated_address, $STRING.text)
LabelAddressMemory.write($TAG.text.replace(':', ''), (generated_address, 'D'))
} | '.word' INTEGER {
generated_address = DataMemory.generate_address()
DataMemory.write(DataMemory.generate_address(),
        int($INTEGER.text))
LabelAddressMemory.write($TAG.text.replace(':', ''), (generated_address, 'D'))
}) ;
data_block: '.data' WS? data (WS? data)* WS? ;
instruction returns [generated_address]: (SYSCALL | R_OPERATION | I_OPERATION
| J_OPERATION) {
generated_address = InstructionMemory.generate_address()
InstructionMemory.write(generated_address, $text.replace('\t', '    '))
$generated_address = generated_address
} ;
instruction_block: TAG WS? instruction {
LabelAddressMemory.write($TAG.text.replace(':', ''), ($instruction.generated_address, 'I'))
} (WS? instruction)* WS? ;
interpret: data_block? '.text' instruction_block+ | COMMENT ;
