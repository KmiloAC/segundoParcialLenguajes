# Generated from IterableFunctions.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,23,93,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,1,0,4,0,24,8,0,11,0,12,0,25,
        1,1,1,1,3,1,30,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,3,5,53,8,5,1,6,1,6,3,6,57,
        8,6,1,6,1,6,1,7,1,7,3,7,63,8,7,1,7,1,7,1,8,1,8,1,8,5,8,70,8,8,10,
        8,12,8,73,9,8,1,9,1,9,1,9,1,9,1,9,3,9,80,8,9,1,9,1,9,1,9,1,9,5,9,
        86,8,9,10,9,12,9,89,9,9,1,10,1,10,1,10,0,1,18,11,0,2,4,6,8,10,12,
        14,16,18,20,0,1,1,0,10,20,91,0,23,1,0,0,0,2,29,1,0,0,0,4,31,1,0,
        0,0,6,38,1,0,0,0,8,45,1,0,0,0,10,52,1,0,0,0,12,54,1,0,0,0,14,60,
        1,0,0,0,16,66,1,0,0,0,18,79,1,0,0,0,20,90,1,0,0,0,22,24,3,2,1,0,
        23,22,1,0,0,0,24,25,1,0,0,0,25,23,1,0,0,0,25,26,1,0,0,0,26,1,1,0,
        0,0,27,30,3,4,2,0,28,30,3,6,3,0,29,27,1,0,0,0,29,28,1,0,0,0,30,3,
        1,0,0,0,31,32,5,1,0,0,32,33,5,2,0,0,33,34,3,8,4,0,34,35,5,3,0,0,
        35,36,3,10,5,0,36,37,5,4,0,0,37,5,1,0,0,0,38,39,5,5,0,0,39,40,5,
        2,0,0,40,41,3,8,4,0,41,42,5,3,0,0,42,43,3,10,5,0,43,44,5,4,0,0,44,
        7,1,0,0,0,45,46,5,6,0,0,46,47,5,22,0,0,47,48,5,7,0,0,48,49,3,18,
        9,0,49,9,1,0,0,0,50,53,3,12,6,0,51,53,3,14,7,0,52,50,1,0,0,0,52,
        51,1,0,0,0,53,11,1,0,0,0,54,56,5,8,0,0,55,57,3,16,8,0,56,55,1,0,
        0,0,56,57,1,0,0,0,57,58,1,0,0,0,58,59,5,9,0,0,59,13,1,0,0,0,60,62,
        5,2,0,0,61,63,3,16,8,0,62,61,1,0,0,0,62,63,1,0,0,0,63,64,1,0,0,0,
        64,65,5,4,0,0,65,15,1,0,0,0,66,71,3,18,9,0,67,68,5,3,0,0,68,70,3,
        18,9,0,69,67,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,71,72,1,0,0,0,72,
        17,1,0,0,0,73,71,1,0,0,0,74,75,6,9,-1,0,75,80,3,8,4,0,76,80,3,10,
        5,0,77,80,5,21,0,0,78,80,5,22,0,0,79,74,1,0,0,0,79,76,1,0,0,0,79,
        77,1,0,0,0,79,78,1,0,0,0,80,87,1,0,0,0,81,82,10,1,0,0,82,83,3,20,
        10,0,83,84,3,18,9,2,84,86,1,0,0,0,85,81,1,0,0,0,86,89,1,0,0,0,87,
        85,1,0,0,0,87,88,1,0,0,0,88,19,1,0,0,0,89,87,1,0,0,0,90,91,7,0,0,
        0,91,21,1,0,0,0,8,25,29,52,56,62,71,79,87
    ]

class IterableFunctionsParser ( Parser ):

    grammarFileName = "IterableFunctions.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'MAP'", "'('", "','", "')'", "'FILTER'", 
                     "'lambda'", "':'", "'['", "']'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'=='", "'!='", "'<'", "'>'", "'<='", 
                     "'>='" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "INTEGER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_mapDeclaration = 2
    RULE_filterDeclaration = 3
    RULE_lambdaFunction = 4
    RULE_iterableObject = 5
    RULE_array = 6
    RULE_tuple = 7
    RULE_expressionList = 8
    RULE_expression = 9
    RULE_binaryOp = 10

    ruleNames =  [ "program", "statement", "mapDeclaration", "filterDeclaration", 
                   "lambdaFunction", "iterableObject", "array", "tuple", 
                   "expressionList", "expression", "binaryOp" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    INTEGER=21
    IDENTIFIER=22
    WS=23

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableFunctionsParser.StatementContext)
            else:
                return self.getTypedRuleContext(IterableFunctionsParser.StatementContext,i)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = IterableFunctionsParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 22
                self.statement()
                self.state = 25 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==1 or _la==5):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mapDeclaration(self):
            return self.getTypedRuleContext(IterableFunctionsParser.MapDeclarationContext,0)


        def filterDeclaration(self):
            return self.getTypedRuleContext(IterableFunctionsParser.FilterDeclarationContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = IterableFunctionsParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 29
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.mapDeclaration()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.filterDeclaration()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MapDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaFunction(self):
            return self.getTypedRuleContext(IterableFunctionsParser.LambdaFunctionContext,0)


        def iterableObject(self):
            return self.getTypedRuleContext(IterableFunctionsParser.IterableObjectContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_mapDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMapDeclaration" ):
                listener.enterMapDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMapDeclaration" ):
                listener.exitMapDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMapDeclaration" ):
                return visitor.visitMapDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def mapDeclaration(self):

        localctx = IterableFunctionsParser.MapDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_mapDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(IterableFunctionsParser.T__0)
            self.state = 32
            self.match(IterableFunctionsParser.T__1)
            self.state = 33
            self.lambdaFunction()
            self.state = 34
            self.match(IterableFunctionsParser.T__2)
            self.state = 35
            self.iterableObject()
            self.state = 36
            self.match(IterableFunctionsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilterDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaFunction(self):
            return self.getTypedRuleContext(IterableFunctionsParser.LambdaFunctionContext,0)


        def iterableObject(self):
            return self.getTypedRuleContext(IterableFunctionsParser.IterableObjectContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_filterDeclaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFilterDeclaration" ):
                listener.enterFilterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFilterDeclaration" ):
                listener.exitFilterDeclaration(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFilterDeclaration" ):
                return visitor.visitFilterDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def filterDeclaration(self):

        localctx = IterableFunctionsParser.FilterDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_filterDeclaration)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(IterableFunctionsParser.T__4)
            self.state = 39
            self.match(IterableFunctionsParser.T__1)
            self.state = 40
            self.lambdaFunction()
            self.state = 41
            self.match(IterableFunctionsParser.T__2)
            self.state = 42
            self.iterableObject()
            self.state = 43
            self.match(IterableFunctionsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LambdaFunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(IterableFunctionsParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(IterableFunctionsParser.ExpressionContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_lambdaFunction

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLambdaFunction" ):
                listener.enterLambdaFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLambdaFunction" ):
                listener.exitLambdaFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLambdaFunction" ):
                return visitor.visitLambdaFunction(self)
            else:
                return visitor.visitChildren(self)




    def lambdaFunction(self):

        localctx = IterableFunctionsParser.LambdaFunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_lambdaFunction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(IterableFunctionsParser.T__5)
            self.state = 46
            self.match(IterableFunctionsParser.IDENTIFIER)
            self.state = 47
            self.match(IterableFunctionsParser.T__6)
            self.state = 48
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IterableObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def array(self):
            return self.getTypedRuleContext(IterableFunctionsParser.ArrayContext,0)


        def tuple_(self):
            return self.getTypedRuleContext(IterableFunctionsParser.TupleContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_iterableObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIterableObject" ):
                listener.enterIterableObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIterableObject" ):
                listener.exitIterableObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIterableObject" ):
                return visitor.visitIterableObject(self)
            else:
                return visitor.visitChildren(self)




    def iterableObject(self):

        localctx = IterableFunctionsParser.IterableObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_iterableObject)
        try:
            self.state = 52
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.array()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.tuple_()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(IterableFunctionsParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray" ):
                return visitor.visitArray(self)
            else:
                return visitor.visitChildren(self)




    def array(self):

        localctx = IterableFunctionsParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(IterableFunctionsParser.T__7)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291780) != 0):
                self.state = 55
                self.expressionList()


            self.state = 58
            self.match(IterableFunctionsParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TupleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expressionList(self):
            return self.getTypedRuleContext(IterableFunctionsParser.ExpressionListContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTuple" ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTuple" ):
                listener.exitTuple(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTuple" ):
                return visitor.visitTuple(self)
            else:
                return visitor.visitChildren(self)




    def tuple_(self):

        localctx = IterableFunctionsParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(IterableFunctionsParser.T__1)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 6291780) != 0):
                self.state = 61
                self.expressionList()


            self.state = 64
            self.match(IterableFunctionsParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableFunctionsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IterableFunctionsParser.ExpressionContext,i)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_expressionList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionList" ):
                listener.enterExpressionList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionList" ):
                listener.exitExpressionList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionList" ):
                return visitor.visitExpressionList(self)
            else:
                return visitor.visitChildren(self)




    def expressionList(self):

        localctx = IterableFunctionsParser.ExpressionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expressionList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.expression(0)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 67
                self.match(IterableFunctionsParser.T__2)
                self.state = 68
                self.expression(0)
                self.state = 73
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lambdaFunction(self):
            return self.getTypedRuleContext(IterableFunctionsParser.LambdaFunctionContext,0)


        def iterableObject(self):
            return self.getTypedRuleContext(IterableFunctionsParser.IterableObjectContext,0)


        def INTEGER(self):
            return self.getToken(IterableFunctionsParser.INTEGER, 0)

        def IDENTIFIER(self):
            return self.getToken(IterableFunctionsParser.IDENTIFIER, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(IterableFunctionsParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(IterableFunctionsParser.ExpressionContext,i)


        def binaryOp(self):
            return self.getTypedRuleContext(IterableFunctionsParser.BinaryOpContext,0)


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = IterableFunctionsParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 18
        self.enterRecursionRule(localctx, 18, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [6]:
                self.state = 75
                self.lambdaFunction()
                pass
            elif token in [2, 8]:
                self.state = 76
                self.iterableObject()
                pass
            elif token in [21]:
                self.state = 77
                self.match(IterableFunctionsParser.INTEGER)
                pass
            elif token in [22]:
                self.state = 78
                self.match(IterableFunctionsParser.IDENTIFIER)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 87
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = IterableFunctionsParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 81
                    if not self.precpred(self._ctx, 1):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 82
                    self.binaryOp()
                    self.state = 83
                    self.expression(2) 
                self.state = 89
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return IterableFunctionsParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBinaryOp" ):
                return visitor.visitBinaryOp(self)
            else:
                return visitor.visitChildren(self)




    def binaryOp(self):

        localctx = IterableFunctionsParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 90
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2096128) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[9] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)
         




