import re

from cstupid.data_objects.cstrule import Rule
from cstupid.data_objects.csttoken import Token

from typing import Iterator, List, Optional, Tuple

class Lexer:
    def __init__(self, rules : List[Rule], ignore_rules : List[Rule]) -> None:
        self.rules = rules
        self.ignores = ignore_rules

    def match(self, rule : Rule, input_string : str) -> Tuple[Optional[Token], str]:
        m = re.match(rule.pattern, input_string)
        if isinstance(m, re.Match):
            input_string = input_string[len(m[0]):]
            return (Token(rule.name, m[0]), input_string)
        else:
            return (None, input_string)
        
    def lex(self, input_string : str) -> Iterator[Token]:
        can_parse : bool = True
        while can_parse and len(input_string) > 0:
            can_parse = False
            ignore_index : int = 0
            while ignore_index < len(self.ignores):
                tok, input_string = self.match(self.ignores[ignore_index], input_string)
                if tok:
                    can_parse = True
                    ignore_index = len(self.ignores)
                    # I won't yield a token here because these tokens have to be ignored
                ignore_index += 1

            # only if none of the self.ignores tokens have been found the Lexer will check the self.rules tokens
            if not can_parse:
                rule_index : int = 0
                while rule_index < len(self.rules):
                    tok, input_string = self.match(self.rules[rule_index], input_string)
                    if tok:
                        can_parse = True
                        rule_index = len(self.rules)
                        yield tok
                    rule_index += 1
            


class LexerGenerator:
    def __init__(self):
        self.rules : List[Rule] = []
        self.ignores : List[Rule] = []

    # add a rule to the lexer generator it should follow
    def add(self, rule_name : str, rule_pattern : str) -> None:
        self.rules.append(Rule(rule_name, rule_pattern))

    # add a rule to the lexer generator it should ignore
    def ignore(self, rule_name : str, rule_pattern : str) -> None:
        self.ignores.append(Rule(rule_name, rule_pattern))

    # build the Lexer from the rules we want_to_use
    def build(self) -> Lexer:
        return Lexer(self.rules, self.ignores)