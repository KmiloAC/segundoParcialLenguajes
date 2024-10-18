# 1. Gramática para Operaciones con Números Racionales

## Descripción

Esta gramática permite realizar operaciones aritméticas entre números racionales, como sumas, restas, multiplicaciones y divisiones.


## Entorno Virtual

Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto. Puedes hacerlo con los siguientes comandos:

```bash
python -m venv venv
source venv/bin/activate  # En Linux
```

Una vez activado el entorno virtual, instala las dependencias necesarias:

```
     pip install antlr4-python3-runtime
```

## Uso

1. Genera el lexer y parser usando ANTLR:

```bash
	antlr4 -Dlanguage=Python3 -visitor RationalExpr.g4
```
Esto generará los archivos necesarios para tu lexer y parser.

2. Ejecuta el programa en Python:

```bash
	python main.py
```

Y aqui ya puedes ingresar las expresiones. Al iniciar el programa nos mostrara un ejemplo de una expresion que puede funcionar.

```
	(6/3 + 2/3)
```