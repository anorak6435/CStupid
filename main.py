import sys
from cstupid.cstlexer import LexerGenerator
from cstupid.cstparser import ParserGenerator

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

pg = ParserGenerator()


stream = Lexer.lex("var Int age := 20;")

print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))
print(next(stream))