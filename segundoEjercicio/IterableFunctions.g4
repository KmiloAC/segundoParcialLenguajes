grammar IterableFunctions;

program : (statement)+ ;

statement 
    : mapDeclaration 
    | filterDeclaration 
    ;

mapDeclaration 
    : 'MAP' '(' lambdaFunction ',' iterableObject ')' 
    ;

filterDeclaration 
    : 'FILTER' '(' lambdaFunction ',' iterableObject ')' 
    ;

lambdaFunction 
    : 'lambda' IDENTIFIER ':' expression 
    ;

iterableObject 
    : array 
    | tuple 
    ;

array 
    : '[' expressionList? ']' 
    ;

tuple 
    : '(' expressionList? ')' 
    ;

expressionList 
    : expression (',' expression)* 
    ;

expression 
    : lambdaFunction 
    | iterableObject 
    | INTEGER 
    | IDENTIFIER 
    | expression binaryOp expression 
    ;

binaryOp 
    : '+' 
    | '-' 
    | '*' 
    | '/' 
    | '%' 
    | '==' 
    | '!=' 
    | '<' 
    | '>' 
    | '<=' 
    | '>=' 
    ;

INTEGER : [0-9]+ ;
IDENTIFIER : [a-zA-Z_][a-zA-Z_0-9]* ;
WS : [ \t\r\n]+ -> skip ;
