grammar Interpreter;

/********* Imports *********/
@parser::header {
from Circuit import Circuit
}

/********* Rules *********/
data[circuit] returns [new_circuit]: TAG WS? ('.asciiz' STRING {
generated_address = $circuit.get_data_memory().generate_address()
$circuit.get_data_memory().write(generated_address, $STRING.text)
$circuit.get_label_address_memory().write($TAG.text.replace(':', ''), (generated_address, 'D'))
} | '.word' INTEGER {
generated_address = $circuit.get_data_memory().generate_address()
$circuit.get_data_memory().write($circuit.get_data_memory().generate_address(),
        int($INTEGER.text))
$circuit.get_label_address_memory().write($TAG.text.replace(':', ''), (generated_address, 'D'))
}) {$new_circuit = $circuit} ;
data_block[circuit] returns [new_circuit]: '.data' WS? data[$circuit] (WS? data[$circuit])* WS? {
$new_circuit = $data.new_circuit
};
instruction[circuit] returns [generated_address, new_circuit]: (SYSCALL | R_OPERATION | I_OPERATION
| J_OPERATION) {
generated_address = $circuit.get_instruction_memory().generate_address()
$circuit.get_instruction_memory().write(generated_address, $text.replace('\t', '    '))
$generated_address = generated_address
} {$new_circuit = $circuit} ;
instruction_block[circuit] returns [new_circuit]: TAG WS? instruction[$circuit] {
$instruction.new_circuit.get_label_address_memory().write($TAG.text.replace(':', ''), ($instruction.generated_address, 'I'))
} (WS? instruction[$circuit])* WS? {
$new_circuit = $instruction.new_circuit
};
interpret returns [circuit]: {
$circuit = Circuit();
}data_block[$circuit]? '.text' {$circuit = $data_block.new_circuit}instruction_block[$circuit]+ {
$circuit = $instruction_block.new_circuit
}| COMMENT ;

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
