# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete listener for a parse tree produced by LaplaceParser.
class LaplaceListener(ParseTreeListener):

    # Enter a parse tree produced by LaplaceParser#program.
    def enterProgram(self, ctx:LaplaceParser.ProgramContext):
        pass

    # Exit a parse tree produced by LaplaceParser#program.
    def exitProgram(self, ctx:LaplaceParser.ProgramContext):
        pass


    # Enter a parse tree produced by LaplaceParser#statement.
    def enterStatement(self, ctx:LaplaceParser.StatementContext):
        pass

    # Exit a parse tree produced by LaplaceParser#statement.
    def exitStatement(self, ctx:LaplaceParser.StatementContext):
        pass


    # Enter a parse tree produced by LaplaceParser#functionDef.
    def enterFunctionDef(self, ctx:LaplaceParser.FunctionDefContext):
        pass

    # Exit a parse tree produced by LaplaceParser#functionDef.
    def exitFunctionDef(self, ctx:LaplaceParser.FunctionDefContext):
        pass


    # Enter a parse tree produced by LaplaceParser#laplaceTransform.
    def enterLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass

    # Exit a parse tree produced by LaplaceParser#laplaceTransform.
    def exitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        pass


    # Enter a parse tree produced by LaplaceParser#expression.
    def enterExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#expression.
    def exitExpression(self, ctx:LaplaceParser.ExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:LaplaceParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:LaplaceParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:LaplaceParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:LaplaceParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#primaryExpression.
    def enterPrimaryExpression(self, ctx:LaplaceParser.PrimaryExpressionContext):
        pass

    # Exit a parse tree produced by LaplaceParser#primaryExpression.
    def exitPrimaryExpression(self, ctx:LaplaceParser.PrimaryExpressionContext):
        pass


    # Enter a parse tree produced by LaplaceParser#functionCall.
    def enterFunctionCall(self, ctx:LaplaceParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LaplaceParser#functionCall.
    def exitFunctionCall(self, ctx:LaplaceParser.FunctionCallContext):
        pass



del LaplaceParser