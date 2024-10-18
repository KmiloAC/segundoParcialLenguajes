# 3. Gramática para la transformada de Laplace

## Descrición

Esta gramática está diseñada para interpretar expresiones matemáticas y calcular la transformada de Laplace de las mismas. El objetivo es analizar expresiones simbólicas y devolver la transformada correspondiente.

# Archivos clave

- LaplaceLexer.g4: Define los tokens para la transformada de Laplace.
- LaplaceParser.g4: Define las reglas sintácticas para interpretar expresiones de la transformada.

# Uso

1. Genera el lexer y parser:

```bash
	antlr4 LaplaceLexer.g4 LaplaceParser.g4
```

2. Ejecuta el programa en Python:

```bash
	python main.py
```

