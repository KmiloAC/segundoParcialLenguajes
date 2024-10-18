# Generated from Laplace.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,13,67,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,1,0,
        1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,7,
        1,8,1,8,1,9,1,9,1,10,4,10,50,8,10,11,10,12,10,51,1,11,1,11,5,11,
        56,8,11,10,11,12,11,59,9,11,1,12,4,12,62,8,12,11,12,12,12,63,1,12,
        1,12,0,0,13,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,
        23,12,25,13,1,0,4,1,0,48,57,3,0,65,90,95,95,97,122,4,0,48,57,65,
        90,95,95,97,122,3,0,9,10,13,13,32,32,69,0,1,1,0,0,0,0,3,1,0,0,0,
        0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,
        15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,
        25,1,0,0,0,1,27,1,0,0,0,3,29,1,0,0,0,5,31,1,0,0,0,7,34,1,0,0,0,9,
        36,1,0,0,0,11,38,1,0,0,0,13,40,1,0,0,0,15,42,1,0,0,0,17,44,1,0,0,
        0,19,46,1,0,0,0,21,49,1,0,0,0,23,53,1,0,0,0,25,61,1,0,0,0,27,28,
        5,40,0,0,28,2,1,0,0,0,29,30,5,41,0,0,30,4,1,0,0,0,31,32,5,58,0,0,
        32,33,5,61,0,0,33,6,1,0,0,0,34,35,5,59,0,0,35,8,1,0,0,0,36,37,5,
        76,0,0,37,10,1,0,0,0,38,39,5,44,0,0,39,12,1,0,0,0,40,41,5,43,0,0,
        41,14,1,0,0,0,42,43,5,45,0,0,43,16,1,0,0,0,44,45,5,42,0,0,45,18,
        1,0,0,0,46,47,5,47,0,0,47,20,1,0,0,0,48,50,7,0,0,0,49,48,1,0,0,0,
        50,51,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,22,1,0,0,0,53,57,7,
        1,0,0,54,56,7,2,0,0,55,54,1,0,0,0,56,59,1,0,0,0,57,55,1,0,0,0,57,
        58,1,0,0,0,58,24,1,0,0,0,59,57,1,0,0,0,60,62,7,3,0,0,61,60,1,0,0,
        0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,65,1,0,0,0,65,66,
        6,12,0,0,66,26,1,0,0,0,4,0,51,57,63,1,6,0,0
    ]

class LaplaceLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    NUMBER = 11
    IDENTIFIER = 12
    WS = 13

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'('", "')'", "':='", "';'", "'L'", "','", "'+'", "'-'", "'*'", 
            "'/'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "IDENTIFIER", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "NUMBER", "IDENTIFIER", "WS" ]

    grammarFileName = "Laplace.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


