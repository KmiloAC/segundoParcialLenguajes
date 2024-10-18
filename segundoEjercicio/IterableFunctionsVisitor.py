# Generated from IterableFunctions.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .IterableFunctionsParser import IterableFunctionsParser
else:
    from IterableFunctionsParser import IterableFunctionsParser

# This class defines a complete generic visitor for a parse tree produced by IterableFunctionsParser.

class IterableFunctionsVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by IterableFunctionsParser#program.
    def visitProgram(self, ctx:IterableFunctionsParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#statement.
    def visitStatement(self, ctx:IterableFunctionsParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#mapDeclaration.
    def visitMapDeclaration(self, ctx:IterableFunctionsParser.MapDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#filterDeclaration.
    def visitFilterDeclaration(self, ctx:IterableFunctionsParser.FilterDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#lambdaFunction.
    def visitLambdaFunction(self, ctx:IterableFunctionsParser.LambdaFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#iterableObject.
    def visitIterableObject(self, ctx:IterableFunctionsParser.IterableObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#array.
    def visitArray(self, ctx:IterableFunctionsParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#tuple.
    def visitTuple(self, ctx:IterableFunctionsParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#expressionList.
    def visitExpressionList(self, ctx:IterableFunctionsParser.ExpressionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#expression.
    def visitExpression(self, ctx:IterableFunctionsParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by IterableFunctionsParser#binaryOp.
    def visitBinaryOp(self, ctx:IterableFunctionsParser.BinaryOpContext):
        return self.visitChildren(ctx)



del IterableFunctionsParser