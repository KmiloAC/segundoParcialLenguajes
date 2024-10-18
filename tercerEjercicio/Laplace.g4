grammar Laplace;

// Entrada principal
program : (statement)+ ;

// Declaraciones de función
statement 
    : functionDef 
    | laplaceTransform 
    ;

// Definición de funciones
functionDef 
    : IDENTIFIER '(' IDENTIFIER ')' ':=' expression ';' 
    ;

// Transformada de Laplace
laplaceTransform 
    : 'L' '(' IDENTIFIER ',' IDENTIFIER ')' ';' 
    ;

// Expresión principal
expression 
    : additiveExpression 
    ;

// Expresiones aditivas
additiveExpression 
    : multiplicativeExpression (('+' | '-') multiplicativeExpression)* 
    ;

// Expresiones multiplicativas
multiplicativeExpression 
    : primaryExpression (('*' | '/') primaryExpression)* 
    ;

// Expresión primaria
primaryExpression
    : NUMBER 
    | IDENTIFIER 
    | '(' expression ')' 
    | functionCall 
    ;

// Llamadas a funciones
functionCall 
    : IDENTIFIER '(' expression ')' 
    ;

// Tokens
NUMBER : [0-9]+ ;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ;
