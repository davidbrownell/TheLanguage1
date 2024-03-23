# Generated from C:/Code/TheLanguage1/src/TheLanguage1/Parser/ANTLR/TheLanguage1.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TheLanguage1Parser import TheLanguage1Parser
else:
    from TheLanguage1Parser import TheLanguage1Parser

# This class defines a complete generic visitor for a parse tree produced by TheLanguage1Parser.

class TheLanguage1Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by TheLanguage1Parser#entry_point__.
    def visitEntry_point__(self, ctx:TheLanguage1Parser.Entry_point__Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguage1Parser#identifier.
    def visitIdentifier(self, ctx:TheLanguage1Parser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TheLanguage1Parser#expression__.
    def visitExpression__(self, ctx:TheLanguage1Parser.Expression__Context):
        return self.visitChildren(ctx)



del TheLanguage1Parser