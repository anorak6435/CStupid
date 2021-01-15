import sys
from cstupid.cstlexer import LexerGenerator
from cstupid.data_objects.cstrule import GrammarNode, Sequence, Optional
from cstupid.cstparser import Parser

# this is to advanced for now
# tree = Parser.parse(Lexer.lex("var Int age := 20; var String name := 'Anorak';"))
lg = LexerGenerator()
lg.ignore("WHITESPACE", r"\s+")
lg.add("VARKEY", "var")
lg.add("ASSIGN", ":=")
lg.add("NUMBER", r"\d+")
lg.add("SEMICOLON", ";")
lg.add("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*")

Lexer = lg.build()

stream = Lexer.lex("var Int age := 20;")


grammar_tree = [GrammarNode("varKey", "VARKEY")]

parser = Parser(grammar_tree)
parser.parse(stream)


# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))
# print(next(stream))