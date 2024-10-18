import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer
from LaplaceParser import LaplaceParser
from LaplaceVisitor import LaplaceVisitor
import sympy as sp


# Clase para manejar las transformadas y las funciones especiales
class LaplaceFunctionHandler:
    def __init__(self):
        self.functions = {}

    def define_function(self, name, expr):
        """Almacena una función en el diccionario."""
        self.functions[name] = expr

    def get_function(self, name):
        """Retorna una función almacenada o lanza una excepción si no existe."""
        if name not in self.functions:
            raise ValueError(f"Function '{name}' is not defined.")
        return self.functions[name]

    def laplace_transform(self, func_name, var_name):
        """Calcula la transformada de Laplace de una función almacenada."""
        if func_name not in self.functions:
            raise ValueError(f"Function '{func_name}' is not defined.")
        t = sp.symbols(var_name)
        f_t = self.functions[func_name]
        s = sp.symbols('s')
        try:
            return sp.laplace_transform(f_t, t, s, noconds=True)
        except Exception as e:
            raise ValueError(f"Error calculating Laplace Transform for {func_name}: {e}")


# Implementación del Visitor
class LaplaceEvalVisitor(LaplaceVisitor):
    def __init__(self, function_handler):
        self.function_handler = function_handler

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitFunctionDef(self, ctx):
        """Define y almacena una nueva función."""
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        expr = self.visit(ctx.expression())
        self.function_handler.define_function(func_name, expr)

    def visitLaplaceTransform(self, ctx):
        """Calcula la transformada de Laplace de una función almacenada."""
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        result = self.function_handler.laplace_transform(func_name, var_name)
        print(f"Laplace Transform of {func_name}({var_name}): {result}")

    def visitNumberExpr(self, ctx):
        return sp.sympify(ctx.NUMBER().getText())

    def visitIdentifierExpr(self, ctx):
        return sp.symbols(ctx.IDENTIFIER().getText())

    def visitAdditiveExpression(self, ctx):
        left = self.visit(ctx.multiplicativeExpression(0))
        for i in range(1, len(ctx.multiplicativeExpression())):
            right = self.visit(ctx.multiplicativeExpression(i))
            if ctx.getChild(2*i-1).getText() == '+':
                left += right
            else:
                left -= right
        return left

    def visitMultiplicativeExpression(self, ctx):
        left = self.visit(ctx.powerExpression(0))
        for i in range(1, len(ctx.powerExpression())):
            right = self.visit(ctx.powerExpression(i))
            if ctx.getChild(2*i-1).getText() == '*':
                left *= right
            else:
                left /= right
        return left

    def visitPowerExpression(self, ctx):
        base = self.visit(ctx.primaryExpression(0))
        if ctx.primaryExpression(1) is not None:
            exponent = self.visit(ctx.primaryExpression(1))
            return base ** exponent
        return base

    def visitPrimaryExpression(self, ctx):
        if ctx.NUMBER():
            return sp.sympify(ctx.NUMBER().getText())
        elif ctx.IDENTIFIER():
            return sp.symbols(ctx.IDENTIFIER().getText())
        elif ctx.getChild(0).getText() == '-':
            return -self.visit(ctx.primaryExpression(0))
        elif ctx.expression():
            return self.visit(ctx.expression())
        else:
            return self.visit(ctx.functionCall())


    def visitNegateExpr(self, ctx):
        return -self.visit(ctx.expr())

    def visitParenthesizedExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitFunctionCallExpr(self, ctx):
        """Llama a funciones especiales o definidas."""
        func_name = ctx.IDENTIFIER().getText()
        arg = self.visit(ctx.expr())

        special_functions = {
            'ideal_delay': lambda x: sp.Heaviside(x) * x,
            'unit_impulse': lambda x: sp.DiracDelta(x),
            'exponential_damping': lambda x: sp.exp(-x),
            'step': lambda x: sp.Heaviside(x),
            'n_power': lambda x: x ** sp.symbols('n'),
            'q_power': lambda x: x ** sp.symbols('q'),
            'log': lambda x: sp.log(x),
            'bessel': lambda x: sp.besselj(1, x),
            'sin': lambda x: sp.sin(x),
            'cos': lambda x: sp.cos(x),
            'sinh': lambda x: sp.sinh(x),
            'cosh': lambda x: sp.cosh(x),
        }

    def visitFunctionDef(self, ctx):
        """Define y almacena una nueva función."""
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        expr = self.visit(ctx.expression())
        print(f"Definiendo función: {func_name}({var_name}) = {expr}")
        self.function_handler.define_function(func_name, expr)
        if func_name in special_functions:
            return special_functions[func_name](arg)
        else:
            raise ValueError(f"Function '{func_name}' is not defined.")


    def visitLaplaceTransform(self, ctx):
        """Calcula la transformada de Laplace de una función almacenada."""
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        result = self.function_handler.laplace_transform(func_name, var_name)
        print(f"Laplace Transform de {func_name}({var_name}): {result}")


        if func_name in special_functions:
            return special_functions[func_name](arg)
        else:
            raise ValueError(f"Function '{func_name}' is not defined.")


def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo de entrada.")
        sys.exit(1)

    input_file = sys.argv[1]
    input_stream = FileStream(input_file)
    lexer = LaplaceLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = LaplaceParser(stream)
    tree = parser.program()

    # Inicializar el manejador de funciones y el visitor
    function_handler = LaplaceFunctionHandler()
    visitor = LaplaceEvalVisitor(function_handler)
    
    # Visitar el árbol
    visitor.visit(tree)


if __name__ == '__main__':
    main()
