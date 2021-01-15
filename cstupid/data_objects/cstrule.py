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
    
    # evaluate the incomming Token
    def evaluate(self, in_tok : Token) -> 'GrammarNode':
        if self.canParse(in_tok):
            return GrammarNode("test", "test")
        else:
            raise SyntaxError(f"Parser expected '{self.name}' but not '{in_tok}'")


# A sequence of grammar nodes is defined as
class Sequence(GrammarNode):
    def __init__(self, name : str, nodes : List[GrammarNode]) -> None:
        self.name = name
        self.nodes = nodes
    
    def canParse(self, tok_list : List[Token]) -> bool:
        token_index = 0
        while token_index < len(self.nodes):
            if not self.nodes[token_index].canParse(tok_list[token_index]):
                raise SyntaxError(f"Parser Sequence expected '{self.name}' bvu")
            token_index += 1
        # If the code get's to this point the sequence could be parsed
            

# Optional grammar nodes are defined as
class Optional(GrammarNode):
    pass

# A Tag is made for the parser to contain a list of rules
# class Tag:
#     def __init__(self, name : str) -> None:
#         self.name = name
#         self.pattern : List[Rule]

#     # check if all consecutive rules match the input string
#     def canParse(self, in_string : str) -> bool:
#         patternIndex = 0
#         # track what rules were matched
#         matched_rules : List[bool] = []
#         while patternIndex < len(self.pattern):
#             matched_rules.append(self.pattern[patternIndex].canParse(in_string))
#             # TODO when a pattern rule matched the in_string has to be updated for the next rule in the list
#             patternIndex += 1
#         return all(matched_rules)

#     def __repr__(self) -> str:
#         return f"(TAG '{self.name}'::'{self.pattern}')"