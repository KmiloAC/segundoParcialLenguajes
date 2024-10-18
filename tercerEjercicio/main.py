import sys
from antlr4 import *
from LaplaceLexer import LaplaceLexer  # Cambiado
from LaplaceParser import LaplaceParser  # Cambiado
from LaplaceVisitor import LaplaceVisitor  # Cambiado
import sympy as sp

class EvalVisitor(LaplaceVisitor):
    def __init__(self):
        self.functions = {}

    def visitProgram(self, ctx):
        return self.visitChildren(ctx)

    def visitStatement(self, ctx):
        return self.visitChildren(ctx)

    def visitFunctionDef(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()  # Nombre de la función
        var_name = ctx.IDENTIFIER(1).getText()    # Variable de la función
        expr = self.visit(ctx.expression())  # Cambiado de ctx.expr() a ctx.expression()
        self.functions[func_name] = expr

    def visitLaplaceTransform(self, ctx):
        func_name = ctx.IDENTIFIER(0).getText()
        var_name = ctx.IDENTIFIER(1).getText()
        if func_name in self.functions:
            t = sp.symbols(var_name)
            f_t = self.functions[func_name]
            s = sp.symbols('s')
            F_s = sp.laplace_transform(f_t, t, s, noconds=True)
            print(f"Laplace Transform of {func_name}({var_name}): {F_s}")
        else:
            print(f"Function {func_name} is not defined.")

    def visitNumberExpr(self, ctx):
        return sp.sympify(ctx.NUMBER().getText())

    def visitIdentifierExpr(self, ctx):
        return sp.symbols(ctx.IDENTIFIER().getText())

    def visitAddSubExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '+':
            return left + right
        else:
            return left - right

    def visitMulDivExpr(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        op = ctx.op.text
        if op == '*':
            return left * right
        else:
            return left / right

    def visitPowerExpr(self, ctx):
        base = self.visit(ctx.expr(0))
        exponent = self.visit(ctx.expr(1))
        return base ** exponent

    def visitNegateExpr(self, ctx):
        value = self.visit(ctx.expr())
        return -value

    def visitParenthesizedExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitFunctionCallExpr(self, ctx):
        func_name = ctx.IDENTIFIER().getText()
        arg = self.visit(ctx.expr())
        if func_name == 'exp':
            return sp.exp(arg)
        elif func_name == 'sin':
            return sp.sin(arg)
        elif func_name == 'cos':
            return sp.cos(arg)
        elif func_name == 'ln':
            return sp.ln(arg)
        elif func_name == 'sinh':
            return sp.sinh(arg)
        elif func_name == 'cosh':
            return sp.cosh(arg)
        elif func_name == 'Heaviside':
            return sp.Heaviside(arg)
        elif func_name == 'DiracDelta':
            return sp.DiracDelta(arg)
        elif func_name == 'sqrt':
            return sp.sqrt(arg)
        else:
            raise Exception(f"Function '{func_name}' is not defined.")

def main():
    if len(sys.argv) < 2:
        print("Por favor, proporciona el nombre del archivo de entrada.")
        sys.exit(1)

    input_file = sys.argv[1]
    input_stream = FileStream(input_file)  # Leer desde un archivo
    lexer = LaplaceLexer(input_stream)  # Cambiado
    stream = CommonTokenStream(lexer)
    parser = LaplaceParser(stream)  # Cambiado
    tree = parser.program()
    visitor = EvalVisitor()
    visitor.visit(tree)

if __name__ == '__main__':
    main()
