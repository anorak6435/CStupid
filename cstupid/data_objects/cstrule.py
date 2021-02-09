# this file will contain the data the parser needs when parsing a grammar

import re
from typing import List
from .csttoken import Token


class TokenRule:
    def __init__(self, name : str, pattern : str) -> None:
        self.name = name
        self.pattern = pattern

    # check if i can parse some input with the pattern inside this rule
    def canParse(self, test_input : str) -> bool:
        return bool(re.match(self.pattern, test_input))


# the base object for the grammar tree
class GrammarNode(object):
    def __init__(self, name : str, pattern : str) -> None:
        self.name = name
        self.pattern = pattern
        # self.children : List[GrammarNode]

    def __repr__(self) -> str:
        return f"NODE({self.name}, {self.pattern})"

    # see if this node can parse the Token
    def canParse(self, in_tok : Token) -> bool:
        return self.pattern == in_tok.name
    
    # evaluate the Token
    # def evaluate(self, in_tok) -> 'GrammarNode':
    #     if self.canParse(in_tok):
    #         return GrammarNode("test", "test")
    #     else:
    #         raise SyntaxError(f"Parser expected '{self.name}' but not '{in_tok}'")


# A sequence of grammar nodes is defined as
class Sequence(GrammarNode):
    def __init__(self, name : str, nodes : List[GrammarNode]) -> None:
        self.name = name
        self.nodes = nodes
        # track the index of the current Node in the list
        self.node_index = 0

    def resetNodeIndex(self) -> None:
        self.node_index = 0
    
    # def canParse(self, in_tok : Token) -> bool:
    #     return_val = self.nodes[self.node_index].canParse(in_tok)
    #     self.node_index += 1
    #     if not return_val:
    #         # reset the node_index if the returnvalue false
    #         self.resetNodeIndex()
    #     # when the node_index is equal to the length of te nodes in the rule
    #     if self.node_index == len(self.nodes):
    #         pass
        # token_index = 0
        # while token_index < len(self.nodes):
        #     if not self.nodes[token_index].canParse(tok_list[token_index]):
        #         return False
        #     token_index += 1
        # # If the code get's to this point the sequence could be parsed
        # return True

    # def evaluate(self, tok_list) -> 'Sequence':
    #     token_index = 0
    #     while token_index < len(self.nodes):
    #         if not self.nodes[token_index].canParse([tok_list[token_index]]):
    #             raise SyntaxError(f"Parser Sequence '{self.name}' expected Node '{self.nodes[token_index]}' bvu")
    #         token_index += 1
    #     # If the code get's to this point the sequence could be parsed
    #     return Sequence("test", [GrammarNode("test", "test")])


# Optional grammar nodes are defined as
class Optional(GrammarNode):
    pass