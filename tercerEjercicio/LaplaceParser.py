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
        4,1,14,85,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,4,0,22,8,0,11,0,12,0,23,1,1,1,1,3,
        1,28,8,1,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,
        1,3,1,3,1,4,1,4,1,5,1,5,1,5,5,5,51,8,5,10,5,12,5,54,9,5,1,6,1,6,
        1,6,5,6,59,8,6,10,6,12,6,62,9,6,1,7,1,7,1,7,3,7,67,8,7,1,8,1,8,1,
        8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,78,8,8,1,9,1,9,1,9,1,9,1,9,1,9,0,0,
        10,0,2,4,6,8,10,12,14,16,18,0,2,1,0,7,8,1,0,9,10,83,0,21,1,0,0,0,
        2,27,1,0,0,0,4,29,1,0,0,0,6,37,1,0,0,0,8,45,1,0,0,0,10,47,1,0,0,
        0,12,55,1,0,0,0,14,63,1,0,0,0,16,77,1,0,0,0,18,79,1,0,0,0,20,22,
        3,2,1,0,21,20,1,0,0,0,22,23,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,
        24,1,1,0,0,0,25,28,3,4,2,0,26,28,3,6,3,0,27,25,1,0,0,0,27,26,1,0,
        0,0,28,3,1,0,0,0,29,30,5,13,0,0,30,31,5,1,0,0,31,32,5,13,0,0,32,
        33,5,2,0,0,33,34,5,3,0,0,34,35,3,8,4,0,35,36,5,4,0,0,36,5,1,0,0,
        0,37,38,5,5,0,0,38,39,5,1,0,0,39,40,5,13,0,0,40,41,5,6,0,0,41,42,
        5,13,0,0,42,43,5,2,0,0,43,44,5,4,0,0,44,7,1,0,0,0,45,46,3,10,5,0,
        46,9,1,0,0,0,47,52,3,12,6,0,48,49,7,0,0,0,49,51,3,12,6,0,50,48,1,
        0,0,0,51,54,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,11,1,0,0,0,54,
        52,1,0,0,0,55,60,3,14,7,0,56,57,7,1,0,0,57,59,3,14,7,0,58,56,1,0,
        0,0,59,62,1,0,0,0,60,58,1,0,0,0,60,61,1,0,0,0,61,13,1,0,0,0,62,60,
        1,0,0,0,63,66,3,16,8,0,64,65,5,11,0,0,65,67,3,16,8,0,66,64,1,0,0,
        0,66,67,1,0,0,0,67,15,1,0,0,0,68,78,5,12,0,0,69,78,5,13,0,0,70,71,
        5,8,0,0,71,78,3,16,8,0,72,73,5,1,0,0,73,74,3,8,4,0,74,75,5,2,0,0,
        75,78,1,0,0,0,76,78,3,18,9,0,77,68,1,0,0,0,77,69,1,0,0,0,77,70,1,
        0,0,0,77,72,1,0,0,0,77,76,1,0,0,0,78,17,1,0,0,0,79,80,5,13,0,0,80,
        81,5,1,0,0,81,82,3,8,4,0,82,83,5,2,0,0,83,19,1,0,0,0,6,23,27,52,
        60,66,77
    ]

class LaplaceParser ( Parser ):

    grammarFileName = "Laplace.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "':='", "';'", "'L'", "','", 
                     "'+'", "'-'", "'*'", "'/'", "'^'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "NUMBER", "IDENTIFIER", "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDef = 2
    RULE_laplaceTransform = 3
    RULE_expression = 4
    RULE_additiveExpression = 5
    RULE_multiplicativeExpression = 6
    RULE_powerExpression = 7
    RULE_primaryExpression = 8
    RULE_functionCall = 9

    ruleNames =  [ "program", "statement", "functionDef", "laplaceTransform", 
                   "expression", "additiveExpression", "multiplicativeExpression", 
                   "powerExpression", "primaryExpression", "functionCall" ]

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
    NUMBER=12
    IDENTIFIER=13
    WS=14

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




    def program(self):

        localctx = LaplaceParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 20
                self.statement()
                self.state = 23 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==5 or _la==13):
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




    def statement(self):

        localctx = LaplaceParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 25
                self.functionDef()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
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




    def functionDef(self):

        localctx = LaplaceParser.FunctionDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 30
            self.match(LaplaceParser.T__0)
            self.state = 31
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 32
            self.match(LaplaceParser.T__1)
            self.state = 33
            self.match(LaplaceParser.T__2)
            self.state = 34
            self.expression()
            self.state = 35
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




    def laplaceTransform(self):

        localctx = LaplaceParser.LaplaceTransformContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_laplaceTransform)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 37
            self.match(LaplaceParser.T__4)
            self.state = 38
            self.match(LaplaceParser.T__0)
            self.state = 39
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 40
            self.match(LaplaceParser.T__5)
            self.state = 41
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 42
            self.match(LaplaceParser.T__1)
            self.state = 43
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




    def expression(self):

        localctx = LaplaceParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
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




    def additiveExpression(self):

        localctx = LaplaceParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.multiplicativeExpression()
            self.state = 52
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==7 or _la==8:
                self.state = 48
                _la = self._input.LA(1)
                if not(_la==7 or _la==8):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 49
                self.multiplicativeExpression()
                self.state = 54
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

        def powerExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LaplaceParser.PowerExpressionContext)
            else:
                return self.getTypedRuleContext(LaplaceParser.PowerExpressionContext,i)


        def getRuleIndex(self):
            return LaplaceParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)




    def multiplicativeExpression(self):

        localctx = LaplaceParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self.powerExpression()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==9 or _la==10:
                self.state = 56
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 57
                self.powerExpression()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PowerExpressionContext(ParserRuleContext):
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
            return LaplaceParser.RULE_powerExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPowerExpression" ):
                listener.enterPowerExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPowerExpression" ):
                listener.exitPowerExpression(self)




    def powerExpression(self):

        localctx = LaplaceParser.PowerExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_powerExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.primaryExpression()
            self.state = 66
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 64
                self.match(LaplaceParser.T__10)
                self.state = 65
                self.primaryExpression()


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

        def primaryExpression(self):
            return self.getTypedRuleContext(LaplaceParser.PrimaryExpressionContext,0)


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




    def primaryExpression(self):

        localctx = LaplaceParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_primaryExpression)
        try:
            self.state = 77
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.match(LaplaceParser.NUMBER)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.match(LaplaceParser.IDENTIFIER)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.match(LaplaceParser.T__7)
                self.state = 71
                self.primaryExpression()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.match(LaplaceParser.T__0)
                self.state = 73
                self.expression()
                self.state = 74
                self.match(LaplaceParser.T__1)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 76
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




    def functionCall(self):

        localctx = LaplaceParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_functionCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(LaplaceParser.IDENTIFIER)
            self.state = 80
            self.match(LaplaceParser.T__0)
            self.state = 81
            self.expression()
            self.state = 82
            self.match(LaplaceParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





