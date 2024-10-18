from fractions import Fraction
from antlr4 import *
from RationalExprLexer import RationalExprLexer
from RationalExprParser import RationalExprParser
from RationalExprVisitor import RationalExprVisitor

# Clase encargada de evaluar expresiones racionales a través de un árbol de análisis.
class EvalVisitor(RationalExprVisitor):

    # Visita el nodo principal (prog) del árbol, que contiene una o más expresiones
    def visitProg(self, ctx):
        # Llama directamente al visitador genérico para la expresión raíz
        return self.visit(ctx.expr())

    # Método para manejar la suma y la resta de dos términos
    def visitAddSub(self, ctx):
        # Evalúa el operando izquierdo y derecho
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # Obtiene el operador matemático ('+' o '-')
        operador = ctx.getChild(1).getText()

        # Realiza la operación correspondiente
        if operador == '+':
            return left + right
        else:
            return left - right

    # Método para manejar multiplicación y división
    def visitMulDiv(self, ctx):
        # Evalúa los operandos izquierdo y derecho
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        # Obtiene el operador ('*' o '/')
        operador = ctx.getChild(1).getText()

        # Realiza la operación de acuerdo al operador
        if operador == '*':
            return left * right
        else:
            return self.dividirOperandos(left, right)

    # Método auxiliar que maneja el intento de dividir dos operandos y controla errores
    def dividirOperandos(self, numerador, denominador):
        try:
            return numerador / denominador
        except ZeroDivisionError:
            print("Error: División por cero detectada.")
            return None

    # Método para manejar fracciones expresadas como a/b
    def visitFraction(self, ctx):
        # Obtiene el texto de la fracción desde el nodo correspondiente
        textoFraccion = ctx.FRACTION().getText()
        # Descompone la fracción en numerador y denominador
        numerador, denominador = map(int, textoFraccion.split('/'))

        # Intenta crear y devolver el valor de la fracción, manejando división por cero
        return self.crearFraccion(numerador, denominador)

    # Método para manejar expresiones entre paréntesis
    def visitParens(self, ctx):
        # Visita la expresión que está dentro de los paréntesis
        return self.visit(ctx.expr())

    # Método que intenta crear una fracción manejando errores de división por cero
    def crearFraccion(self, numerador, denominador):
        try:
            return Fraction(numerador, denominador)
        except ZeroDivisionError:
            print("Error: No se puede crear una fracción con denominador cero.")
            return None

# Función que procesa la entrada del usuario desde un archivo
def procesarArchivoEntrada(input_file):
    with open(input_file, 'r') as file:
        for line in file:
            expresion = line.strip()
            if expresion:  # Solo procesa líneas no vacías
                print(f"Evaluando expresión: {expresion}")
                resultado = analizarYEvaluarExpresion(expresion)
                if resultado is not None:
                    print(f"= {resultado}")

# Función que procesa la entrada del usuario desde el input estándar
def procesarEntradaUsuario():
    while True:
        try:
            # Recibe la expresión del usuario
            expresionUsuario = input('Ejemplo entrada: (2/3 + 1/3)\nDigite su expresión: ').strip()
            if not expresionUsuario:
                continue

            # Analiza y evalúa la expresión ingresada por el usuario
            resultado = analizarYEvaluarExpresion(expresionUsuario)

            # Si el resultado no es nulo, lo imprime
            if resultado is not None:
                print(f"= {resultado}")

        except EOFError:
            print("\nFin de la entrada del usuario. Saliendo...")
            break
        except Exception as e:
            print(f"Error detectado: {e}")

# Función que analiza y evalúa la expresión ingresada
def analizarYEvaluarExpresion(expresion):
    # Convierte la expresión en un flujo de entrada para ANTLR
    input_stream = InputStream(expresion)

    # Genera el lexer y el parser para procesar la entrada
    lexer = RationalExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RationalExprParser(token_stream)

    # Analiza la expresión generando un árbol
    tree = parser.prog()

    # Crea un visitante para evaluar el árbol de análisis
    visitor = EvalVisitor()
    return visitor.visit(tree)

# Punto de entrada del programa
if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        procesarArchivoEntrada(input_file)  # Procesa el archivo de entrada
    else:
        procesarEntradaUsuario()  # Procesa la entrada del usuario
