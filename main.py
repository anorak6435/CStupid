import sys
from cstupid.cstlexer import LexerGenerator
from cstupid.data_objects.cstrule import GrammarNode, Sequence, Optional
from cstupid.cst_const_tokens import *
from cstupid.cstparser import Parser

# this is to advanced for now
# tree = Parser.parse(Lexer.lex("var Int age := 20; var String name := 'Anorak';"))
lg = LexerGenerator()
lg.ignore(TT_NEWLINE, "\n")
lg.ignore(TT_WHITESPACE, r"\s+")
lg.add(TT_VARKEY, "var")
lg.add(TT_ECHOKEY, "echo")
lg.add(TT_ASSIGN, "=")
lg.add(TT_NUMBER, r"\d+")
lg.add(TT_LPAREN, "\(")
lg.add(TT_RPAREN, "\)")
lg.add(TT_SEMICOLON, ";")
lg.add(TT_COLON, ":")
lg.add(TT_STRING, "\".+?\"")
lg.add(TT_IDENTIFIER, r"[a-zA-Z_][a-zA-Z0-9_]*")

Lexer = lg.build()

# stream = Lexer.lex("""var name : String = "anorak";
# var age : Int = 14; """)
stream = Lexer.lex("""echo("Hello world!"); var greeting : String = "Hello Anorak"; echo(greeting);""")
# semanticly wrong variable declaration
# stream = Lexer.lex("""var name : Int = "anorak";""") # make sure this line will be caught
print(stream)

# print("start dump!")
# for x in stream:
#     print(x)
# print("end dump!")
# grammar_tree = [GrammarNode("varKey", "VARKEY")]
parser = Parser(stream)
parser.parse()