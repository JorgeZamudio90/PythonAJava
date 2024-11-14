grammar PythonToJava;

program: (func_def | stmt)*;

func_def: 'def' NAME '(' params? ')' ':' stmt*;

params: NAME (',' NAME)*;

stmt: var_assign | return_stmt | print_stmt;

var_assign: NAME '=' expr;

return_stmt: 'return' expr;

print_stmt: 'print' '(' expr (',' expr)* ')';

expr: expr ('+'|'-'|'*'|'/') expr
     | NUMBER
     | NAME
     | NAME '(' expr (',' expr)* ')'
     | '(' expr ')';

NAME: [a-zA-Z_][a-zA-Z_0-9]*;
NUMBER: [0-9]+;

WS: [ \t\r\n]+ -> skip;