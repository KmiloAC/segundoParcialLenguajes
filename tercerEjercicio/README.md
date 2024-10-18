# 3. Gramática para la transformada de Laplace

## Descrición

Esta gramática está diseñada para interpretar expresiones matemáticas y calcular la transformada de Laplace de las mismas. El objetivo es analizar expresiones simbólicas y devolver la transformada correspondiente.

## Archivos clave

- LaplaceLexer.g4: Define los tokens para la transformada de Laplace.
- LaplaceParser.g4: Define las reglas sintácticas para interpretar expresiones de la transformada.

### Aclaración

En mi caso primero tuve que crear el entorno virtual, lo que es recomendable, para entrar a este en mi caso se hace de la siguiente manera:

```bash
source ~/myenvs/myenv/bin/activate
```

## Instalar Sympy

Sympy es una biblioteca de Python para matemáticas simbólicas. Por lo que va a ser necesaria y se instala de la siguiente manera, dentro de nuestro entorno virtual

```bash
pip install sympy
```

# Uso


1. Genera el lexer y parser:

```bash
antlr4 -Dlanguage=Python3 -visitor Laplace.g4
```

2. Ejecuta el programa en Python:

```bash
python main.py archivo.txt
```

Como se puede notar funciona de la misma forma que los demàs.

