# 2. Gramática para Funciones Funcionales (MAP, FILTER)

## Descripción

Esta gramática  permite la implementación de funciones como MAP y FILTER en listas o tuplas. Las funciones son aplicables a cada elemento de un iterable para mapear o filtrar valores basados en condiciones.

# Uso

### Aclaración

En mi caso primero tuve que crear el entorno virtual, lo que es recomendable, para entrar a este en mi caso se hace de la siguiente manera:

```bash
source ~/myenvs/myenv/bin/activate
```

1. Genera el lexer y parser:

```bash
antlr4 -Dlanguage=Python3 -visitor IterableFunctions.g4
```

2. Llama al programa y el archivo de entrada, que usted puede modificar o crear uno nuevo y lo llama dentro de la consola:

```bash
	python main.py entrada1.txt
```