# Generated from C:/Code/TheLanguage1/src/TheLanguage1/Parser/ANTLR/TheLanguage1.g4 by ANTLR 4.13.1
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
        4,1,13,25,2,0,7,0,2,1,7,1,2,2,7,2,1,0,5,0,8,8,0,10,0,12,0,11,9,0,
        1,0,5,0,14,8,0,10,0,12,0,17,9,0,1,0,1,0,1,1,1,1,1,2,1,2,1,2,0,0,
        3,0,2,4,0,0,23,0,9,1,0,0,0,2,20,1,0,0,0,4,22,1,0,0,0,6,8,5,2,0,0,
        7,6,1,0,0,0,8,11,1,0,0,0,9,7,1,0,0,0,9,10,1,0,0,0,10,15,1,0,0,0,
        11,9,1,0,0,0,12,14,3,4,2,0,13,12,1,0,0,0,14,17,1,0,0,0,15,13,1,0,
        0,0,15,16,1,0,0,0,16,18,1,0,0,0,17,15,1,0,0,0,18,19,5,0,0,1,19,1,
        1,0,0,0,20,21,5,11,0,0,21,3,1,0,0,0,22,23,5,11,0,0,23,5,1,0,0,0,
        2,9,15
    ]

class TheLanguage1Parser ( Parser ):

    grammarFileName = "TheLanguage1.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'('", "')'", "'['", "']'", "'from'", 
                     "'import'" ]

    symbolicNames = [ "<INVALID>", "HORIZONTAL_WHITESPACE", "NEWLINE", "NESTED_NEWLINE", 
                      "LINE_CONTINUATION", "LPAREN", "RPAREN", "LBRACK", 
                      "RBRACK", "INCLUDE_FROM", "INCLUDE_IMPORT", "IDENTIFIER", 
                      "INDENT", "DEDENT" ]

    RULE_entry_point__ = 0
    RULE_identifier = 1
    RULE_expression__ = 2

    ruleNames =  [ "entry_point__", "identifier", "expression__" ]

    EOF = Token.EOF
    HORIZONTAL_WHITESPACE=1
    NEWLINE=2
    NESTED_NEWLINE=3
    LINE_CONTINUATION=4
    LPAREN=5
    RPAREN=6
    LBRACK=7
    RBRACK=8
    INCLUDE_FROM=9
    INCLUDE_IMPORT=10
    IDENTIFIER=11
    INDENT=12
    DEDENT=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Entry_point__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(TheLanguage1Parser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(TheLanguage1Parser.NEWLINE)
            else:
                return self.getToken(TheLanguage1Parser.NEWLINE, i)

        def expression__(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TheLanguage1Parser.Expression__Context)
            else:
                return self.getTypedRuleContext(TheLanguage1Parser.Expression__Context,i)


        def getRuleIndex(self):
            return TheLanguage1Parser.RULE_entry_point__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEntry_point__" ):
                return visitor.visitEntry_point__(self)
            else:
                return visitor.visitChildren(self)




    def entry_point__(self):

        localctx = TheLanguage1Parser.Entry_point__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_entry_point__)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==2:
                self.state = 6
                self.match(TheLanguage1Parser.NEWLINE)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 12
                self.expression__()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 18
            self.match(TheLanguage1Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IdentifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TheLanguage1Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TheLanguage1Parser.RULE_identifier

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifier" ):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)




    def identifier(self):

        localctx = TheLanguage1Parser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.match(TheLanguage1Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression__Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(TheLanguage1Parser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return TheLanguage1Parser.RULE_expression__

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression__" ):
                return visitor.visitExpression__(self)
            else:
                return visitor.visitChildren(self)




    def expression__(self):

        localctx = TheLanguage1Parser.Expression__Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression__)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self.match(TheLanguage1Parser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





