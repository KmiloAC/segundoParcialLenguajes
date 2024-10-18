grammar RationalExpr;

// Reglas del parser
prog    : expr EOF ;              // La entrada comienza con una expresión y finaliza con EOF

expr    : expr '+' expr   # AddSub    // Suma de dos expresiones
        | expr '-' expr   # AddSub    // Resta de dos expresiones
        | expr '*' expr   # MulDiv    // Multiplicación de dos expresiones
        | expr '/' expr   # MulDiv    // División de dos expresiones
        | '(' expr ')'    # Parens    // Expresiones entre paréntesis
        | FRACTION        # Fraction  // Fracciones como 'a/b'
        ;

// Reglas del lexer
FRACTION : [0-9]+ '/' [0-9]+ ;    // Fracciones como 'a/b'
WS      : [ \t\r\n]+ -> skip ;    // Ignorar espacios en blanco y saltos de línea
