from cstupid.data_objects.cstast import VarDeclar, CNumber, Node
from cstupid.data_objects.cstrule import TokenRule, GrammarNode
from cstupid.data_objects.csttoken import Token
from typing import List, Iterator, Callable, Optional

class Parser:
    def __init__(self, defined_rules : List[GrammarNode]) -> None:
        # keep track of what rules are defined in the parser
        self.defined_rules = defined_rules


    # create a tree from the stream of tokens given. using the rules we defined
    def parse(self, stream : Iterator[Token]) -> List[Node]:
        # keep track of what tag I am trying to resolve
        for tok in stream:
            print(self.defined_rules[0].canParse(tok))
            print(tok)
            

        




# pg = ParserGenerator()

# @pg.production("main : statements")
# def statements(s):
#     return s[0]

# @pg.production("statements : statement statements")
# def some_statement(s):
#     return s[0]

# @pg.production("statements : statement")
# def handle_single_statement(s):
#     return s[0]

# @pg.production("statement : expr ")
# def expression(s):
#     return s[0]

# @pg.production("expr : VARKEY IDENTIFIER IDENTIFIER ASSIGN expr SEMICOLON")
# def vardeclar(s):
#     return VarDeclar(s[1], s[2], s[4])

# @pg.production("expr : NUMBER")
# def handle_number_expression(s):
#     return CNumber(s[0])

# @pg.error
# def error_handler(token):
#     raise ValueError("Ran into a %s where it was't expected" % token.gettokentype())
# Parser = pg.build()