# Generated from RationalExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RationalExprParser import RationalExprParser
else:
    from RationalExprParser import RationalExprParser

# This class defines a complete listener for a parse tree produced by RationalExprParser.
class RationalExprListener(ParseTreeListener):

    # Enter a parse tree produced by RationalExprParser#prog.
    def enterProg(self, ctx:RationalExprParser.ProgContext):
        pass

    # Exit a parse tree produced by RationalExprParser#prog.
    def exitProg(self, ctx:RationalExprParser.ProgContext):
        pass


    # Enter a parse tree produced by RationalExprParser#AddSub.
    def enterAddSub(self, ctx:RationalExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by RationalExprParser#AddSub.
    def exitAddSub(self, ctx:RationalExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by RationalExprParser#MulDiv.
    def enterMulDiv(self, ctx:RationalExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by RationalExprParser#MulDiv.
    def exitMulDiv(self, ctx:RationalExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by RationalExprParser#Parens.
    def enterParens(self, ctx:RationalExprParser.ParensContext):
        pass

    # Exit a parse tree produced by RationalExprParser#Parens.
    def exitParens(self, ctx:RationalExprParser.ParensContext):
        pass


    # Enter a parse tree produced by RationalExprParser#Fraction.
    def enterFraction(self, ctx:RationalExprParser.FractionContext):
        pass

    # Exit a parse tree produced by RationalExprParser#Fraction.
    def exitFraction(self, ctx:RationalExprParser.FractionContext):
        pass



del RationalExprParser