# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LaplaceParser import LaplaceParser
else:
    from LaplaceParser import LaplaceParser

# This class defines a complete generic visitor for a parse tree produced by LaplaceParser.

class LaplaceVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LaplaceParser#program.
    def visitProgram(self, ctx:LaplaceParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#statement.
    def visitStatement(self, ctx:LaplaceParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#functionDef.
    def visitFunctionDef(self, ctx:LaplaceParser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#laplaceTransform.
    def visitLaplaceTransform(self, ctx:LaplaceParser.LaplaceTransformContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#expression.
    def visitExpression(self, ctx:LaplaceParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:LaplaceParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:LaplaceParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:LaplaceParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LaplaceParser#functionCall.
    def visitFunctionCall(self, ctx:LaplaceParser.FunctionCallContext):
        return self.visitChildren(ctx)



del LaplaceParser