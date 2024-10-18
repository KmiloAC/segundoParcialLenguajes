# Generated from RationalExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalExprParser import RationalExprParser
else:
    from RationalExprParser import RationalExprParser

# This class defines a complete generic visitor for a parse tree produced by RationalExprParser.

class RationalExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RationalExprParser#prog.
    def visitProg(self, ctx:RationalExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalExprParser#AddSub.
    def visitAddSub(self, ctx:RationalExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalExprParser#MulDiv.
    def visitMulDiv(self, ctx:RationalExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalExprParser#Parens.
    def visitParens(self, ctx:RationalExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RationalExprParser#Fraction.
    def visitFraction(self, ctx:RationalExprParser.FractionContext):
        return self.visitChildren(ctx)



del RationalExprParser