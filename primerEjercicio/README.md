# 1. Gramática para Operaciones con Números Racionales

## Descripción

Esta gramática permite realizar operaciones aritméticas entre números racionales, como sumas, restas, multiplicaciones y divisiones.


## Entorno Virtual

Es recomendable crear un entorno virtual para gestionar las dependencias del proyecto. Puedes hacerlo con los siguientes comandos:

```bash
python -m venv venv
source venv/bin/activate 
```

Una vez activado el entorno virtual, instala las dependencias necesarias:

```
pip install antlr4-python3-runtime
```

## Uso

### Aclaración

En mi caso primero tuve que crear el entorno virtual como mostre anteriormente, lo que es recomendable, para entrar a este en mi caso se hace de la siguiente manera:

```bash
source ~/myenvs/myenv/bin/activate
```

1. Genera el lexer y parser usando ANTLR:

```bash
antlr4 -Dlanguage=Python3 -visitor RationalExpr.g4
```
Esto generará los archivos necesarios para tu lexer y parser.

2. Ejecuta el programa en Python:


```bash
python main.py entrada1.txt
```

Y podras ingresar tus propias operaciones o testear distintas situaciones con un archivo.txt. Al iniciar el programa nos mostrara un ejemplo de una expresion que puede funcionar. Como de igual manera puedes ver otras en el archivo de texto

```
(6/3 + 2/3)
```

