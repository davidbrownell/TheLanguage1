// ----------------------------------------------------------------------
// |
// |  TheLanguage1.g4
// |
// |  David Brownell <db@DavidBrownell.com>
// |      2024-03-23 12:27:14
// |
// ----------------------------------------------------------------------
// |
// |  Copyright David Brownell 2024
// |  Distributed under the MIT License.
// |
// ----------------------------------------------------------------------
grammar TheLanguage1;

// ----------------------------------------------------------------------
tokens { INDENT, DEDENT }

@lexer::header {

from antlr_denter.DenterHelper import DenterHelper
from TheLanguage1Parser import TheLanguage1Parser

}

@lexer::members {

def CustomInit(self):
    self._nested_pair_ctr = 0


class TheLanguage1Denter(DenterHelper):
    def __init__(self, lexer, *args, **kwargs):
        super().__init__(lexer, *args, **kwargs, should_ignore_eof=False)

        self.lexer: TheLanguage1Lexer = lexer

    def pull_token(self):
        return super(TheLanguage1Denter, self.lexer).nextToken()


def nextToken(self):
    if not hasattr(self, "_denter"):
        self._denter = self.__class__.TheLanguage1Denter(
            self,
            TheLanguage1Parser.NEWLINE,
            TheLanguage1Parser.INDENT,
            TheLanguage1Parser.DEDENT,
        )

    return self._denter.nextToken()
}


// ----------------------------------------------------------------------
// |
// |  Lexer Rules
// |
// ----------------------------------------------------------------------
HORIZONTAL_WHITESPACE:                      [ \t]+ -> channel(HIDDEN);

// ----------------------------------------------------------------------
// Newlines nested within paired brackets are safe to ignore, but newlines outside of paired
// brackets are meaningful.
NEWLINE:                                    '\r'? '\n' {self._nested_pair_ctr == 0}? [ \t]*;
NESTED_NEWLINE:                             '\r'? '\n' {self._nested_pair_ctr != 0}? [ \t]* -> channel(HIDDEN);

LINE_CONTINUATION:                          '\\' '\r'? '\n' [ \t]* -> channel(HIDDEN);

LPAREN:                                     '(' {self._nested_pair_ctr += 1};
RPAREN:                                     ')' {self._nested_pair_ctr -= 1};
LBRACK:                                     '[' {self._nested_pair_ctr += 1};
RBRACK:                                     ']' {self._nested_pair_ctr -= 1};

// ----------------------------------------------------------------------
INCLUDE_FROM:                               'from';
INCLUDE_IMPORT:                             'import';

// TODO: We really want this to be any char that isn't defined elsewhere (not just emojis)
IDENTIFIER:                                 '_'* [a-zA-Z\p{Emoji}][a-zA-Z0-9_\p{Emoji}]* '?'? '!'? '_'*;


// ----------------------------------------------------------------------
// |
// |  Parser Rules
// |
// ----------------------------------------------------------------------
// Note that any rule with a '__' suffix represents a non-binding rule (meaning a rule without
// backing code only here for organizational purposes).

entry_point__:                              NEWLINE* expression__* EOF;

// ----------------------------------------------------------------------
// |  Common
identifier:                                 IDENTIFIER;

// ----------------------------------------------------------------------
// |  Expressions
expression__:                               (IDENTIFIER); // BugBug
