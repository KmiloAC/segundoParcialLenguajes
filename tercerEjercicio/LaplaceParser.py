# Generated from Laplace.g4 by ANTLR 4.13.2
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
        4,1,13,76,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,4,0,20,8,0,11,0,12,0,21,1,1,1,1,3,1,26,8,1,
        1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,
        1,4,1,4,1,5,1,5,1,5,5,5,49,8,5,10,5,12,5,52,9,5,1,6,1,6,1,6,5,6,
        57,8,6,10,6,12,6,60,9,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,3,7,69,8,7,1,
        8,1,8,1,8,1,8,1,8,1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,2,1,0,7,8,1,
        0,9,10,73,0,19,1,0,0,0,2,25,1,0,0,0,4,27,1,0,0,0,6,35,1,0,0,0,8,
        43,1,0,0,0,10,45,1,0,0,0,12,53,1,0,0,0,14,68,1,0,0,0,16,70,1,0,0,
        0,18,20,3,2,1,0,19,18,1,0,0,0,20,21,1,0,0,0,21,19,1,0,0,0,21,22,
        1,0,0,0,22,1,1,0,0,0,23,26,3,4,2,0,24,26,3,6,3,0,25,23,1,0,0,0,25,
        24,1,0,0,0,26,3,1,0,0,0,27,28,5,12,0,0,28,29,5,1,0,0,29,30,5,12,
        0,0,30,31,5,2,0,0,31,32,5,3,0,0,32,33,3,8,4,0,33,34,5,4,0,0,34,5,
        1,0,0,0,35,36,5,5,0,0,36,37,5,1,0,0,37,38,5,12,0,0,38,39,5,6,0,0,
        39,40,5,12,0,0,40,41,5,2,0,0,41,42,5,4,0,0,42,7,1,0,0,0,43,44,3,
        10,5,0,44,9,1,0,0,0,45,50,3,12,6,0,46,47,7,0,0,0,47,49,3,12,6,0,
        48,46,1,0,0,0,49,52,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,11,1,
        0,0,0,52,50,1,0,0,0,53,58,3,14,7,0,54,55,7,1,0,0,55,57,3,14,7,0,
        56,54,1,0,0,0,57,60,1,0,0,0,58,56,1,0,0,0,58,59,1,0,0,0,59,13,1,
        0,0,0,60,58,1,0,0,0,61,69,5,11,0,0,62,69,5,12,0,0,63,64,5,1,0,0,
        64,65,3,8,4,0,65,66,5,2,0,0,66,69,1,0,0,0,67,69,3,16,8,0,68,61,1,
        0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,67,1,0,0,0,69,15,1,0,0,0,70,
        71,5,12,0,0,71,72,5,1,0,0,72,73,3,8,4,0,73,74,5,2,0,0,74,17,1,0,
        0,0,5,21,25,50,58,68
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "';'", "'L'", "','", 
                     "'+'", "'-'", "'*'", "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "NUMBER", "IDENTIFIER", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDef = 2
    RULE_laplaceTransform = 3
    RULE_expression = 4
    RULE_additiveExpression = 5
    RULE_multiplicativeExpression = 6
    RULE_primaryExpression = 7
    RULE_functionCall = 8

    ruleNames =  [ "program", "statement", "functionDef", "laplaceTransform", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "primaryExpression", "functionCall" ]

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
    NUMBER=11
    IDENTIFIER=12
    WS=13

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
                return self.getTypedRuleContexts(LaplaceParser.StatementContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.StatementContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_program

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

        localctx = LaplaceParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.statement()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==12):
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

        def functionDef(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionDefContext,0)


        def laplaceTransform(self):
            return self.getTypedRuleContext(LaplaceParser.LaplaceTransformContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_statement

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

        localctx = LaplaceParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 23
                self.functionDef()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                self.laplaceTransform()
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


    class FunctionDefContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceParser.IDENTIFIER)
            else:
                return self.getToken(LaplaceParser.IDENTIFIER, i)

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_functionDef

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDef" ):
                listener.enterFunctionDef(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDef" ):
                listener.exitFunctionDef(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDef" ):
                return visitor.visitFunctionDef(self)
            else:
                return visitor.visitChildren(self)




    def functionDef(self):

        localctx = LaplaceParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 28
            self.match(LaplaceParser.T__0)
            self.state = 29
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 30
            self.match(LaplaceParser.T__1)
            self.state = 31
            self.match(LaplaceParser.T__2)
            self.state = 32
            self.expression()
            self.state = 33
            self.match(LaplaceParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LaplaceTransformContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LaplaceParser.IDENTIFIER)
            else:
                return self.getToken(LaplaceParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LaplaceParser.RULE_laplaceTransform

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLaplaceTransform" ):
                listener.enterLaplaceTransform(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLaplaceTransform" ):
                listener.exitLaplaceTransform(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLaplaceTransform" ):
                return visitor.visitLaplaceTransform(self)
            else:
                return visitor.visitChildren(self)




    def laplaceTransform(self):

        localctx = LaplaceParser.LaplaceTransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_laplaceTransform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(LaplaceParser.T__4)
            self.state = 36
            self.match(LaplaceParser.T__0)
            self.state = 37
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 38
            self.match(LaplaceParser.T__5)
            self.state = 39
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 40
            self.match(LaplaceParser.T__1)
            self.state = 41
            self.match(LaplaceParser.T__3)
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

        def additiveExpression(self):
            return self.getTypedRuleContext(LaplaceParser.AdditiveExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_expression

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




    def expression(self):

        localctx = LaplaceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.additiveExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.MultiplicativeExpressionContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = LaplaceParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.multiplicativeExpression()
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 46
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 47
                self.multiplicativeExpression()
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.PrimaryExpressionContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.PrimaryExpressionContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = LaplaceParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.primaryExpression()
            self.state = 58
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 54
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 55
                self.primaryExpression()
                self.state = 60
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(LaplaceParser.NUMBER, 0)

        def IDENTIFIER(self):
            return self.getToken(LaplaceParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LaplaceParser.FunctionCallContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = LaplaceParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_primaryExpression)
        try:
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 61
                self.match(LaplaceParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 62
                self.match(LaplaceParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 63
                self.match(LaplaceParser.T__0)
                self.state = 64
                self.expression()
                self.state = 65
                self.match(LaplaceParser.T__1)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 67
                self.functionCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LaplaceParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LaplaceParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LaplaceParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = LaplaceParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 71
            self.match(LaplaceParser.T__0)
            self.state = 72
            self.expression()
            self.state = 73
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





